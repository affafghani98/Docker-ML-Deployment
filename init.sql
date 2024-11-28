-- init.sql
CREATE DATABASE IF NOT EXISTS Model_Logger;

USE Model_Logger;

CREATE TABLE IF NOT EXISTS Log (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Current_Date_Time DATETIME DEFAULT CURRENT_TIMESTAMP,
    Input_Params TEXT,
    Output TEXT,
    Response_Time FLOAT
);

