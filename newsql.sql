CREATE DATABASE PYTHON;
USE PYTHON;
CREATE TABLE BANK(ACCOUNT_NO INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(30) UNIQUE,LOGIN_PASSWORD VARCHAR(30),
 TRANSACTION_PASSWORD VARCHAR(30))AUTO_INCREMENT=1001;
CREATE TABLE ACCOUNT_TRANSACTION(
TRANSACTION_ID INT PRIMARY KEY auto_increment,ACCOUNT_NO INT,UPID  VARCHAR(20),
AMOUNT DECIMAL(10,2),TRANSACTION_DATE timestamp DEFAULT current_timestamp(),
FOREIGN KEY(ACCOUNT_NO) REFERENCES BANK(ACCOUNT_NO));
select*from bank; 
SELECT * FROM ACCOUNT_TRANSACTION;
drop table bank; 
DROP TABLE ACCOUNT_TRANSACTION;