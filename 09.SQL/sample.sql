-- Создайте новую базу данных:
CREATE DATABASE IF NOT EXISTS footballers;

-- начнём работу с базой данных:
USE footballers;

-- Добавим новую таблицу, в которой для каждого футболиста будем хранить следующую информацию:
-- id – уникальный идентификатор, который будет служить первичным ключом таблицы ( числовое значение, обязательное, автозаполняемое)
-- first_name – имя (строковое значение, до 30 символов, обязательное)
-- last_name - фамилия (строковое значение, до 30 символов, обязательное)
-- year_of_birth – год рождения
CREATE TABLE IF NOT EXISTS players (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
	first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
	year_of_birth YEAR
);

-- добавим в неё несколько игроков:
INSERT INTO players ( id, first_name, last_name) VALUES ( null, 'Artem', 'Dzyuba');
INSERT INTO players ( id, first_name, last_name, year_of_birth) VALUES ( null, 'Igor', 'Akinfeev', 1986);
INSERT INTO players ( id, first_name, last_name, year_of_birth) VALUES ( null, 'Denis', 'Cheryshev', 1990);
INSERT INTO players ( id, first_name, last_name, year_of_birth) VALUES ( null, 'Igor', 'Smolnikov', 1988);

SELECT first_name, last_name FROM footballers.players;

-- Запросите данные по футболистам, год рождения которых мы знаем:
SELECT * FROM footballers.players WHERE year_of_birth IS NOT NULL;

-- Изменим информацию об Артёме, добавив год его рождения при помощи команды UPDATE:
UPDATE players
SET year_of_birth=1988
WHERE id=1;

-- получить имена и фамилии футболистов, которые родились после 1987 года:
SELECT first_name, last_name FROM players WHERE year_of_birth > 1987;

-- добавить информацию о клубах, за которые играют эти ребята. Можно было бы просто добавить в таблицу  players новую колонку  team, но мы так делать не будем. В соответствии с правилами нормализации баз данных нам стоит добавить новую сущность «teams», создать соответствующую таблицу и добавить связь между записями в этой таблице и футболистами.
CREATE TABLE IF NOT EXISTS teams (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key, 
	team_name VARCHAR(20)
);

-- Добавим клубы:
INSERT INTO teams (id, team_name) VALUES (null, 'Zenit');
INSERT INTO teams (id, team_name) VALUES (null, 'CSKA');
INSERT INTO teams (id, team_name) VALUES (null, 'Villarreal');

-- Добавим новое поле в таблицу players при помощи команды ALTER TABLE:
ALTER TABLE players ADD team_id INTEGER NOT NULL;

-- Установим связь между футболистами и их клубами:
UPDATE players SET team_id=1 WHERE id IN (1,4);
UPDATE players SET team_id=2 WHERE id=2;
UPDATE players SET team_id=3 WHERE id=3;

-- Выведем всех футболистов вместе с их клубами. Для этого воспользуемся таким инструментов, как присоединение (JOIN):
SELECT player.first_name, player.last_name, team.team_name
FROM players player
INNER JOIN teams team ON player.team_id=team.id;


