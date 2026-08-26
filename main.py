from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from database.db import obtener_conexion
import random
import string

app = FastAPI()

# Montar archivos estáticos (CSS, JS) y el motor de plantillas HTML
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Modelo de datos que espera recibir la petición POST desde el frontend
class URLRequest(BaseModel):
    url_larga: str  

def generar_codigo_corto(length=6):
    """Genera una cadena aleatoria alfanumérica de tamaño fijo para el código corto."""
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(length))

@app.get("/", response_class=HTMLResponse)
def leer_raiz(request: Request):
    """Renderiza y devuelve la página principal (index.html)."""
    return templates.TemplateResponse(request, "index.html")

@app.post("/acortar")
def acortar_url(data: URLRequest):
    """Recibe la URL larga, valida su formato, evita duplicados y genera un código corto."""
    url_original = data.url_larga.strip()
    
    # Validación básica de formato HTTP/HTTPS
    if not url_original.startswith("http://") and not url_original.startswith("https://"):
        raise HTTPException(status_code=400, detail="La URL debe comenzar con http:// o https://")

    conn = obtener_conexion()
    cursor = conn.cursor()

    # Verificar si la URL ya existe en la base de datos para evitar duplicados
    cursor.execute("SELECT url_codigo_corto FROM url_direccion WHERE url_original = ?", (url_original,))
    resultado = cursor.fetchone()

    if resultado:
        codigo_corto = resultado[0]
        conn.close()
        return {"url_corta": f"http://127.0.0.1:8000/{codigo_corto}"}

    # Si no existe, generar un código único que no colisione en la base de datos
    while True:
        codigo_corto = generar_codigo_corto()
        cursor.execute("SELECT url_id FROM url_direccion WHERE url_codigo_corto = ?", (codigo_corto,))
        if not cursor.fetchone():
            break

    # Insertar la nueva relación URL original / código corto en SQL Server
    cursor.execute(
        "INSERT INTO url_direccion (url_original, url_codigo_corto) VALUES (?, ?)",
        (url_original, codigo_corto)
    )
    conn.commit()
    conn.close()

    return {"url_corta": f"http://127.0.0.1:8000/{codigo_corto}"}

@app.get("/{codigo_corto}")
def redirigir(codigo_corto: str, request: Request):
    """Busca el código corto y redirige al usuario a la URL original correspondiente."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    
    cursor.execute("SELECT url_original FROM url_direccion WHERE url_codigo_corto = ?", (codigo_corto,))
    resultado = cursor.fetchone()
    conn.close()

    if not resultado:
        raise HTTPException(status_code=404, detail="Enlace no encontrado")
    
    url_original = resultado[0]
    return RedirectResponse(url_original)