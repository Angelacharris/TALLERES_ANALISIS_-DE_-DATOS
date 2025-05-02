create database Angelatienda;
use Angelatienda;

-- Crear la tabla Categorías
CREATE TABLE Categorias (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(50)
);

-- Crear la tabla Productos
CREATE TABLE Productos (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Precio DECIMAL(10, 2)
);

-- Crear la tabla Productos_Categorías para la relación muchos a muchos
CREATE TABLE Productos_Categorias (
    ProductoID INT,
    CategoriaID INT,
    PRIMARY KEY (ProductoID, CategoriaID),
    FOREIGN KEY (ProductoID) REFERENCES Productos(ID),
    
-- Insertar categorías
INSERT INTO Categorias (ID, Nombre) VALUES (1, 'Bebidas');
INSERT INTO Categorias (ID, Nombre) VALUES (2, 'Dulces');

-- Insertar productos
INSERT INTO Productos (ID, Nombre, Precio) VALUES (1, 'cafe', 1.50);
INSERT INTO Productos (ID, Nombre, Precio) VALUES (2, 'Caramelo', 0.80);
INSERT INTO Productos (ID, Nombre, Precio) VALUES (3, 'leche', 2.00);

-- Relacionar productos con categorías
INSERT INTO Productos_Categorias (ProductoID, CategoriaID) VALUES (1, 1); -- cafe en Bebidas
INSERT INTO Productos_Categorias (ProductoID, CategoriaID) VALUES (2, 2); -- Caramelo en Dulces
INSERT INTO Productos_Categorias (ProductoID, CategoriaID) VALUES (3, 1); -- leche en Bebidas