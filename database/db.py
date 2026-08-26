import pyodbc

def obtener_conexion():
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=127.0.0.1,1433;"
        "DATABASE=TaupDB;"
        "UID=sa;"
        "PWD=TuPassword123;"
    )
    return pyodbc.connect(conn_str)