# open database editor:
# 	create database "Interview"
# 	create table [Person] (
# 				personID int
# 				, name unicode string(100)
# 				, age decimal
# 				, nationalityID int
# 				, birthDate datetime
# 				)
# 		make personID as primary key
# -------------------------------------------
# Checking CRUD Form/Page capabilities
# -------------------------------------------
# create form/page
# 	bind it to [Person] table from database with a binding source
# 	Add all fields with retrive command
# 	insert some fields
# 	save 3 persons
# -------------------------------------------
# Checking List Form/Page capabilities
# -------------------------------------------
# create form/page
# 	insert a grid control and link it to [Person] table
# 	make it show all the person table data
# 	insert a button in each line, that when u click the button it will open the details page of the row



CREATE TABLE Person (
id INT,
name varchar(100) 
age int,
nationalityID int,
last_login DATETIME,
)   

-- insert values into the Users table.
INSERT INTO Users
VALUES