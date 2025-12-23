
create DATABASE MEET ;

USE MEET;

CREATE TABLE  MEETEMPLOYEES (
    EMPID INT PRIMARY KEY,
    NAME VARCHAR(50),
    SALARY DECIMAL(10,2),
    DEPARTMENT VARCHAR(50),
    JOININGDATE DATE
);

INSERT INTO MEETEMPLOYEES (EMPID, NAME, SALARY, DEPARTMENT, JOININGDATE)
VALUES
(1, 'John Smith', 55000, 'HR', '2022-03-15'),
(2, 'Alice Brown', 62000, 'Finance', '2021-07-10'),
(3, 'Michael Johnson', 48000, 'IT', '2023-01-05'),
(4, 'Sarah Wilson', 70000, 'Marketing', '2020-11-20'),
(5, 'David Lee', 53000, 'Operations', '2022-06-01'),
(6, 'Emma Davis', 61000, 'IT', '2021-09-18'),
(7, 'Robert Miller', 58000, 'HR', '2019-05-12'),
(8, 'Sophia Taylor', 75000, 'Finance', '2020-02-25'),
(9, 'Daniel Anderson', 49500, 'Support', '2023-04-08'),
(10, 'Olivia Thomas', 68000, 'Sales', '2021-12-03');



SELECT DEPARTMENT 



