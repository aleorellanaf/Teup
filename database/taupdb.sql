IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'TaupDB')
BEGIN
    CREATE DATABASE TaupDB;
END
GO

USE TaupDB;
GO

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'url_direccion')
BEGIN
    CREATE TABLE url_direccion (
        id INT IDENTITY(1,1) PRIMARY KEY,
        url_original NVARCHAR(MAX) NOT NULL,
        url_codigo_corto VARCHAR(10) NOT NULL UNIQUE,
        clicks INT NOT NULL DEFAULT 0,
        creado_en DATETIME NOT NULL DEFAULT GETDATE()
    );
END
GO
