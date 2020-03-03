-- script that creates the table
-- unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT '1', UNIQUE INDEX(id), name VARCHAR(256));
