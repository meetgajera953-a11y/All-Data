
CREATE DATABASE DataDigger;
USE DataDigger;

--------------------------------------------------
-- 1. Customers Table
--------------------------------------------------
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(50),
    Email VARCHAR(100),
    Address VARCHAR(100)
);


INSERT INTO Customers VALUES
(1,'Alice','alice@gmail.com','Mumbai'),
(2,'Bob','bob@gmail.com','Delhi'),
(3,'Charlie','charlie@gmail.com','Pune'),
(4,'David','david@gmail.com','Ahmedabad'),
(5,'Emma','emma@gmail.com','Bangalore');


SELECT * FROM Customers;


UPDATE Customers SET Address='Surat' WHERE CustomerID=2;


DELETE FROM Customers WHERE CustomerID=5;


SELECT * FROM Customers WHERE Name='Alice';

--------------------------------------------------
-- 2. Orders Table
--------------------------------------------------
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount INT
);

-- Orders table me 5 records insert
INSERT INTO Orders VALUES
(101,1,'2024-01-10',60000),
(102,2,'2024-01-15',15000),
(103,3,'2024-02-01',2500),
(104,1,'2024-02-10',800),
(105,4,'2024-03-01',500);


SELECT * FROM Orders WHERE CustomerID=1;


UPDATE Orders SET TotalAmount=65000 WHERE OrderID=101;


DELETE FROM Orders WHERE OrderID=105;


SELECT * FROM Orders WHERE OrderDate >= '2024-02-01';


SELECT MAX(TotalAmount) FROM Orders;


SELECT MIN(TotalAmount) FROM Orders;


SELECT AVG(TotalAmount) FROM Orders;

--------------------------------------------------
-- 3. Products Table
--------------------------------------------------
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Price INT,
    Stock INT
);

-- Products insert
INSERT INTO Products VALUES
(1,'Laptop',60000,10),
(2,'Mobile',15000,20),
(3,'Headphones',2000,15),
(4,'Keyboard',800,0),
(5,'Mouse',500,25);

SELECT * FROM Products ORDER BY Price DESC;


UPDATE Products SET Price=1800 WHERE ProductID=3;


DELETE FROM Products WHERE Stock=0;


SELECT * FROM Products WHERE Price BETWEEN 500 AND 2000;

SELECT MAX(Price) FROM Products;


SELECT MIN(Price) FROM Products;

--------------------------------------------------
-- 4. OrderDetails Table
--------------------------------------------------
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    SubTotal INT
);

-- Order details insert
INSERT INTO OrderDetails VALUES
(1,101,1,1,60000),
(2,101,3,1,2000),
(3,102,2,1,15000),
(4,103,5,5,2500),
(5,104,4,1,800);

-- Specific order details
SELECT * FROM OrderDetails WHERE OrderID=101;

-- Total revenue calculate karna
SELECT SUM(SubTotal) FROM OrderDetails;

-- Top 3 most ordered products
SELECT ProductID, SUM(Quantity) 
FROM OrderDetails 
GROUP BY ProductID 
ORDER BY SUM(Quantity) DESC 
LIMIT 3;


SELECT COUNT(ProductID) 
FROM OrderDetails 
WHERE ProductID=1;