-- create database called amit
/*
create database called amit
*/

CREATE DATABASE AMIT;

USE AMIT;
-- create table 

CREATE TABLE Students (
	-- column name datatype,
	studentid INT PRIMARY KEY,
	studentName VARCHAR(50),
	Age INT
);

-- INSERT VALUES

INSERT INTO Students (studentid , studentName , Age)
VALUES (1,'Amit',30),(2,'sameh',20),(3,'learning',40);

-- print table 

SELECT * FROM Students;