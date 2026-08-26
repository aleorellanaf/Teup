from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from database.db import obtener_conexion
import random
import string

app = FastAPI()

# Montar archivos estáticos y templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class URLRequest(BaseModel):
    url: str  # Recibimos como string para validar manualmente

def generar_codigo_corto(length=6):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(length))

@app.get("/", response_class=HTMLResponse)
def leer_raiz(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/acortar")
def acortar_url(data: URLRequest):
    url_original = data.url.strip()
    
    # 1. Validación básica de formato
    if not url_original.startswith("http://") and not url_original.startswith("https://"):
        raise HTTPException(status_code=400, detail="La URL debe comenzar con http:// o https://")

    conn = obtener_conexion()
    cursor = conn.cursor()

    # 2. Verificar si la URL ya existe en la base de datos para evitar duplicados
    cursor.execute("SELECT url_codigo_corto FROM url_direccion WHERE url_original = ?", (url_original,))
    resultado = cursor.fetchone()

    if resultado:
        # Si ya existe, retornamos el código que ya tenía asignado
        codigo_corto = resultado[0]
        conn.close()
        return {"codigo_corto": codigo_corto}

    # 3. Si no existe, generamos un código único nuevo
    while True:
        codigo_corto = generar_codigo_corto()
        cursor.execute("SELECT url_id FROM url_direccion WHERE url_codigo_corto = ?", (codigo_corto,))
        if not cursor.fetchone():
            break

    # 4. Insertar en SQL Server
    cursor.execute(
        "INSERT INTO url_direccion (url_original, url_codigo_corto) VALUES (?, ?)",
        (url_original, codigo_corto)
    )
    conn.commit()
    conn.close()

    return {"codigo_corto": codigo_corto}

@app.get("/{codigo_corto}")
def redirigir(codigo_corto: str, request: Request):
    conn = obtener_conexion()
    cursor = conn.cursor()
    
    cursor.execute("SELECT url_original FROM url_direccion WHERE url_codigo_corto = ?", (codigo_corto,))
    resultado = cursor.fetchone()
    conn.close()

    if not resultado:
        raise HTTPException(status_code=404, detail="Enlace no encontrado")
    
    url_original = resultado[0]
    return RedirectResponse(url_original)