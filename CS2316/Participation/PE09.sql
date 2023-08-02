drop database if exists PE09;
create database PE09;
use PE09;

create table characters (
	characterID int primary key,
	name varchar(225),
	skill varchar(225),
	age int,
	actorID int
);    
create table colors (
	actorID int primary key,
	name varchar(225),
	numEpisodes int,
	numCharacters int
);