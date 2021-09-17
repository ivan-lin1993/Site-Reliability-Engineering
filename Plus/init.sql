CREATE DATABASE `employee`;



CREATE TABLE `employee`.`employees`
(
	`username` varchar(50) NOT NULL, 
	`email` varchar(50) NULL,
	`mobile` varchar(50) NULL,
	`title` varchar(50) NOT NULL,
	`department` varchar(50) NOT NULL,
	PRIMARY KEY (`username`)
);

INSERT INTO `employee`.`employees` values ('ivan.lin', 'ivan@email.com','0909123456','Developer','RD');