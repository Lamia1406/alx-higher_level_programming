-- creates the MySQL server user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED  BY 'user_0d_2_pwd';
-- grant only SELECT privilege to the user user_0d_2
GRANT SELECT
ON  `hbtn_0d_2`.* 
TO 'user_0d_2'@'localhost';
-- create a database  hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
