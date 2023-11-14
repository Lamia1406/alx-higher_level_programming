-- lists all the tables of a database in your MySQL server
-- INFORMATION_SCHEMA :a MySQL system database that contains metadata about other databases on the server
USE INFORMATION_SCHEMA;
-- TABLE_NAME: contains the names of the tables in the specified database.
SELECT TABLE_NAME AS Tables_in_mysql
-- TABLES: a table within INFORMATION_SCHEMA contains information about all tables in all databases.
FROM TABLES
-- This condition filters the results to only include tables from the current database. 
WHERE TABLE_SCHEMA = DATABASE();
