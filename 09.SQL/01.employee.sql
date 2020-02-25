CREATE DATABASE IF NOT EXISTS employee;

USE employee;

CREATE TABLE IF NOT EXISTS staff (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
	first_name VARCHAR(30) NOT NULL,
  last_name VARCHAR(30) NOT NULL
);

INSERT INTO staff (id, first_name, last_name) VALUES (null, 'Artem', 'Dzyuba');
INSERT INTO staff (id, first_name, last_name) VALUES (null, 'Igor', 'Akinfeev');
INSERT INTO staff (id, first_name, last_name) VALUES (null, 'Denis', 'Cheryshev');
INSERT INTO staff (id, first_name, last_name) VALUES (null, 'Igor', 'Smolnikov');

CREATE TABLE IF NOT EXISTS positions (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key, 
	position_name VARCHAR(20)
);

INSERT INTO positions (id, position_name) VALUES (null, 'striker');
INSERT INTO positions (id, position_name) VALUES (null, 'captain');
INSERT INTO positions (id, position_name) VALUES (null, 'goalkeeper');
INSERT INTO positions (id, position_name) VALUES (null, 'left winger');
INSERT INTO positions (id, position_name) VALUES (null, 'right-back');

CREATE TABLE IF NOT EXISTS salary (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key, 
	month_salary INT
);


INSERT INTO salary (id, month_salary) VALUES (null, '400 000');
INSERT INTO salary (id, month_salary) VALUES (null, '267 000');
INSERT INTO salary (id, month_salary) VALUES (null, '91 667');
INSERT INTO salary (id, month_salary) VALUES (null, '183 333');
