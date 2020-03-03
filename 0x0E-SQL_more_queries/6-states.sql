-- create a data base and a table
CREATE IF NOT EXISTS DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE IF NOT EXISTS TABLE states
(id INTEGER PRIMARY KEY, name VARCHAR(256) NOT NULL);
