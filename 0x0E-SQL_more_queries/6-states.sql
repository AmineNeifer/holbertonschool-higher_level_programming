-- create a data base and a table
CREATE DATABASE IF NOT EXISTS DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS TABLE states
(id INTEGER PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL,
name VARCHAR(256) NOT NULL);
