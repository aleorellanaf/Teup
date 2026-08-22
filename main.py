from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import secrets
import string
from database.db import obtener_conexion

app = FastAPI()

# 1. Configurar FastAPI para que lea la carpeta "static"
app.mount("/static", StaticFiles(directory="static"), name="static")

class UrlData(BaseModel):
    url_larga: str

def generar_codigo():
    caracteres = string.ascii_letters + string.digits
    return ''.join(secrets.choice(caracteres) for _ in range(6))

# 2. Cargar el HTML desde la carpeta "templates"
@app.get("/")
def cargar_interfaz():
    return FileResponse("templates/index.html")

# 3. Endpoint para acortar
@app.post("/acortar")
def acortar_url(data: UrlData, request: Request):
    codigo = generar_codigo()
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO url_direccion (url_original, url_codigo_corto) VALUES (?, ?)", 
        (data.url_larga, codigo)
    )
    conn.commit()
    conn.close()
    
    base = str(request.base_url).rstrip("/")
    return {"url_corta": f"{base}/{codigo}"}

# 4. Endpoint de redirección
@app.get("/{codigo}")
def redirigir(codigo: str):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT url_original FROM url_direccion WHERE url_codigo_corto = ?", (codigo,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return RedirectResponse(url=row[0])
    raise HTTPException(status_code=404, detail="URL no encontrada")