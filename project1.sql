-- ===============================
-- DATABASE
-- ===============================
CREATE DATABASE DataDigger;
USE DataDigger;

-- ===============================
-- CUSTOMERS
-- ===============================
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

-- ===============================
-- PRODUCTS
-- ===============================
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Price INT,
    Stock INT
);

INSERT INTO Products VALUES
(1,'Laptop',60000,10),
(2,'Mobile',15000,20),
(3,'Headphones',2000,15),
(4,'Keyboard',800,0),
(5,'Mouse',500,25);

-- ===============================
-- ORDERS
-- ===============================
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

INSERT INTO Orders VALUES
(101,1,'2024-01-10',60000),
(102,2,'2024-01-15',15000),
(103,3,'2024-02-01',2500),
(104,1,'2024-02-10',800),
(105,4,'2024-03-01',500);

-- ===============================
-- ORDER DETAILS
-- ===============================
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    SubTotal INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

INSERT INTO OrderDetails VALUES
(1,101,1,1,60000),
(2,101,3,1,2000),
(3,102,2,1,15000),
(4,103,5,5,2500),
(5,104,4,1,800);

-- =================================================
-- 🔥 ALL 22 QUERIES
-- =================================================

-- 1
SELECT * FROM Customers;

-- 2
SELECT * FROM Customers WHERE Name='Alice';

-- 3
UPDATE Customers SET Address='Surat' WHERE CustomerID=2;

-- 4
DELETE FROM Customers WHERE CustomerID=5;

-- 5
SELECT * FROM Orders;

-- 6
SELECT * FROM Orders WHERE CustomerID=1;

-- 7
UPDATE Orders SET TotalAmount=65000 WHERE OrderID=101;

-- 8
DELETE FROM Orders WHERE OrderID=105;

-- 9
SELECT * FROM Orders WHERE OrderDate >= '2024-02-01';

-- 10
SELECT MAX(TotalAmount) FROM Orders;

-- 11
SELECT MIN(TotalAmount) FROM Orders;

-- 12
SELECT AVG(TotalAmount) FROM Orders;

-- 13
SELECT * FROM Products ORDER BY Price DESC;

-- 14
UPDATE Products SET Price=1800 WHERE ProductID=3;

-- 15
DELETE FROM Products WHERE Stock=0;

-- 16
SELECT * FROM Products WHERE Price BETWEEN 500 AND 2000;

-- 17
SELECT MAX(Price) FROM Products;

-- 18
SELECT MIN(Price) FROM Products;

-- 19
SELECT * FROM OrderDetails WHERE OrderID=101;

-- 20
SELECT SUM(SubTotal) AS TotalRevenue FROM OrderDetails;

-- 21
SELECT ProductID, SUM(Quantity) AS TotalQty
FROM OrderDetails
GROUP BY ProductID
ORDER BY TotalQty DESC
LIMIT 3;

-- 22
SELECT COUNT(ProductID) FROM OrderDetails WHERE ProductID=1;