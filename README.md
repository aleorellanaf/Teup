# 🔗 Taup - Acortador de URLs

Taup es una aplicación web moderna y ligera para acortar enlaces, desarrollada con un stack robusto que combina un backend en **FastAPI**, persistencia de datos en **SQL Server** y una interfaz web limpia y minimalista.

---

## 🚀 Características

* **Acortamiento rápido:** Convierte URLs largas en enlaces cortos al instante.
* **Prevención de duplicados:** Si una URL ya ha sido acortada anteriormente, el sistema detecta su existencia en la base de datos y reutiliza el código asignado en lugar de duplicar registros.
* **Redirección automática:** Permite redireccionar de manera fluida desde el código corto hacia la URL original.
* **Validación de formato:** Asegura que los enlaces ingresados comiencen estrictamente con `http://` o `https://`.
* **Interfaz amigable:** Diseño moderno en tonos degradados con barra de búsqueda tipo píldora y copiado rápido al portapapeles.

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python, FastAPI, Uvicorn, Pydantic, Jinja2.
* **Base de Datos:** Microsoft SQL Server (vía Docker o instalación nativa) mediante `pyodbc`.
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla).

---

## 📂 Estructura del Proyecto

```text
Teup/
├── database/
│   ├── db.py           # Conexión centralizada a SQL Server
│   └── setup.sql       # Script de creación de base de datos y tablas
├── static/
│   ├── app.js          # Lógica asíncrona del frontend (Fetch API)
│   └── styles.css      # Estilos modernos de la interfaz
├── templates/
│   └── index.html      # Plantilla principal de la interfaz web
├── main.py             # Aplicación principal de FastAPI y rutas
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Documentación del proyecto


⚙️ Configuración y Puesta en Marcha
1. Clonar el repositorio
Abre tu terminal y ejecuta:

Bash
git clone [https://github.com/aleorellanaf/Teup.git](https://github.com/aleorellanaf/Teup.git)
cd Teup
2. Instalar las dependencias de Python
Asegúrate de tener Python instalado y ejecuta:

Bash
pip install -r requirements.txt
3. Configuración de la Base de Datos según tu Sistema Operativo
🍏 Opción A: macOS (Usando Docker)
Asegúrate de tener Docker Desktop abierto.

Levanta el contenedor oficial de SQL Server ejecutando:

Bash
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=TuPassword123" -p 1433:1433 --name sqlserver -d [mcr.microsoft.com/mssql/server:2022-latest](https://mcr.microsoft.com/mssql/server:2022-latest)
Conéctate a tu contenedor mediante tu gestor de base de datos preferido y ejecuta el script ubicado en database/setup.sql para crear la base de datos TaupDB y la tabla requerida.

💻 Opción B: Windows (Usando SQL Server Nativo)
Asegúrate de tener SQL Server instalado de forma local y el ODBC Driver 17 for SQL Server de Microsoft instalado en tu PC.

Abre SQL Server Management Studio (SSMS), asegúrate de utilizar el usuario sa con la contraseña TuPassword123 (o ajusta las credenciales en database/db.py según tu configuración local).

Ejecuta el script del archivo database/setup.sql para crear la base de datos TaupDB y la tabla url_direccion.

4. Ejecutar el servidor de desarrollo
Inicia la aplicación utilizando Uvicorn con recarga automática:

En macOS / Linux:

Bash
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
En Windows (CMD o PowerShell):

Bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Una vez iniciado el servidor, abre tu navegador favorito e ingresa a:

http://127.0.0.1:8000