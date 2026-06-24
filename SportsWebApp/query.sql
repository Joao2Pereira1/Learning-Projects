-- Active: 1721650497174@@127.0.0.1@3306@sport
CREATE DATABASE sport;
CREATE TABLE registrants (
    name char(20),
    sport char(20) );

INSERT INTO registrants (name,sport) VALUES ("sad", "asdsd");

SELECT * FROM registrants;