CREATE DATABASE TaupDB;
GO
USE TaupDB;
GO

CREATE TABLE url_direccion (
    url_id INT IDENTITY(1,1) PRIMARY KEY,
    url_original VARCHAR(MAX) NOT NULL,
    url_codigo_corto VARCHAR(50) NOT NULL UNIQUE
);
GO