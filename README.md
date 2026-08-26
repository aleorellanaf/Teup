# 🔗 Taup - Acortador de URLs

Taup es una aplicación web moderna y ligera para acortar enlaces, desarrollada con un stack robusto que combina un backend en **FastAPI**, persistencia de datos en **SQL Server (vía Docker)** y una interfaz web limpia y minimalista.

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
* **Base de Datos:** Microsoft SQL Server (ejecutándose en Docker) mediante `pyodbc`.
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