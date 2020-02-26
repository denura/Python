-- Задание 1. Создайте БД для хранения информации о сотрудниках. Для каждого сотрудника будем хранить следующую информацию:
-- •	Имя
-- •	Фамилия
-- •	Должность
-- •	Зарплата
-- Все поля обязательные и не могут быть пустыми. У каждого сотрудника может быть только одна должность, могут быть сотрудники с одинаковыми должностями.
-- Добавьте 3-5 записей в каждую таблицу.

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
	position_name VARCHAR(20) NOT NULL
);

INSERT INTO positions (id, position_name) VALUES (null, 'striker');
INSERT INTO positions (id, position_name) VALUES (null, 'captain');
INSERT INTO positions (id, position_name) VALUES (null, 'goalkeeper');
INSERT INTO positions (id, position_name) VALUES (null, 'left winger');
INSERT INTO positions (id, position_name) VALUES (null, 'right-back');

CREATE TABLE IF NOT EXISTS salary (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key, 
	month_salary INT NOT NULL
);

INSERT INTO salary (id, month_salary) VALUES (null, 400000);
INSERT INTO salary (id, month_salary) VALUES (null, 267000);
INSERT INTO salary (id, month_salary) VALUES (null, 91667);
INSERT INTO salary (id, month_salary) VALUES (null, 183333);

ALTER TABLE staff ADD salary_id INTEGER NOT NULL;
ALTER TABLE staff ADD position_id INTEGER NOT NULL;

UPDATE staff SET position_id=2 WHERE id=1;
UPDATE staff SET position_id=2 WHERE id=2;
UPDATE staff SET position_id=4 WHERE id=3;
UPDATE staff SET position_id=5 WHERE id=4;

-- Задание 2. Составьте запросы на выборку данных (SELECT):
-- •	Все сотрудники с зарплатами меньше 300 000 рублей.

SELECT staff.first_name, staff.last_name, salary.month_salary
FROM staff
INNER JOIN salary ON staff.salary_id=salary_id where month_salary < 300000;

-- •	Всех сотрудники, занимающие определённую должность (например - captain), с зарплатой меньше 300 000 рублей.
SELECT staff.first_name, staff.last_name, salary.month_salary
FROM staff
INNER JOIN salary ON staff.salary_id=salary_id where month_salary < 300000 and position_name == 'captain';
