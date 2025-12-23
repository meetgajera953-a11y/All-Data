CREATE database TASK1;

USE TASK1;

-- Students Table
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    marks INT,
    city VARCHAR(50)
);

-- Employees Table
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    salary INT,
    department VARCHAR(50),
    joining_date DATE
);

INSERT INTO Students VALUES
(1, 'Amit', 20, 85, 'Delhi'),
(2, 'Riya', 21, 72, 'Mumbai'),
(3, 'Karan', 22, 65, 'Delhi'),
(4, 'Neha', 20, 90, 'Delhi'),
(5, 'Rahul', 23, 55, 'Mumbai'),
(6, 'Simran', 21, 78, 'Chennai');

INSERT INTO Employees VALUES
(101, 'Raj', 25000, 'HR', '2022-01-10'),
(102, 'Anita', 45000, 'IT', '2021-03-15'),
(103, 'Vikas', 30000, 'Finance', '2020-07-20'),
(104, 'Priya', 55000, 'IT', '2019-11-05'),
(105, 'Suresh', 28000, 'HR', '2023-02-01');


SELECT * FROM Students;

SELECT name, marks FROM Students;



-- Students with marks greater than 70
SELECT * FROM Students WHERE marks > 70;

-- Students from Delhi
SELECT * FROM Students WHERE city = 'Delhi';

-- Employees with salary less than 30000
SELECT * FROM Employees WHERE salary < 30000;



-- Students from Delhi AND marks > 60
SELECT * FROM Students
WHERE city = 'Delhi' AND marks > 60;

-- Employees in HR OR IT department
SELECT * FROM Employees
WHERE department = 'HR' OR department = 'IT';

-- Students NOT from Mumbai
SELECT * FROM Students
WHERE NOT city = 'Mumbai';


-- Students ordered by marks (descending)
SELECT * FROM Students
ORDER BY marks DESC;

-- Employees ordered by salary (ascending)
SELECT * FROM Employees
ORDER BY salary ASC;



-- Top 5 students based on marks
SELECT * FROM Students
ORDER BY marks DESC
LIMIT 5;

-- First 3 employees
SELECT * FROM Employees
LIMIT 3;



-- Total number of employees in each department
SELECT department, COUNT(*) AS total_employees
FROM Employees
GROUP BY department;

-- Average salary of each department
SELECT department, AVG(salary) AS avg_salary
FROM Employees
GROUP BY department;


-- Departments with average salary > 40000
SELECT department, AVG(salary) AS avg_salary
FROM Employees
GROUP BY department
HAVING AVG(salary) > 40000;

-- Cities having more than 2 students
SELECT city, COUNT(*) AS total_students
FROM Students
GROUP BY city
HAVING COUNT(*) > 2;


-- Maximum marks scored by students
SELECT MAX(marks) AS max_marks FROM Students;

-- Minimum salary among employees
SELECT MIN(salary) AS min_salary FROM Employees;

-- Average marks of all students
SELECT AVG(marks) AS avg_marks FROM Students;

-- Total number of students
SELECT COUNT(*) AS total_students FROM Students;

