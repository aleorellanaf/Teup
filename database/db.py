import pyodbc

def obtener_conexion():
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;" 
        "DATABASE=TaupDB;"
        "Trusted_Connection=yes;"
    )
    return pyodbc.connect(conn_str)