-- creates a table called second_table in the current database in your MySQL server.
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
-- create these records
INSERT INTO second_table VALUES(1, "John", 10);
INSERT INTO second_table VALUES(2, "Alex", 3);
INSERT INTO second_table VALUES(3, "Bob", 14);
INSERT INTO second_table VALUES(4, "George", 8);
