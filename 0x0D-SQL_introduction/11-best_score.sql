-- lists score, name from all rows  with score >= 10 of the table second_table from the database hbtn_0c_0 in your MySQL server ordered by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score desc;
