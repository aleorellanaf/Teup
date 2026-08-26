import pyodbc

def obtener_conexion():
    """
    Establece y retorna una conexión activa con la base de datos TaupDB
    en SQL Server utilizando el driver ODBC 17.
    """
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=127.0.0.1,1433;"
        "DATABASE=TaupDB;"
        "UID=sa;"
        "PWD=TuPassword123;"
    )
    return pyodbc.connect(conn_str)