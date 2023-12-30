DROP TABLE IF EXISTS teams;

CREATE TABLE IF NOT EXISTS teams (
	id SERIAL,
	teamname varchar(50) DEFAULT NULL,
	when_changed varchar(30) DEFAULT NULL,
	when_created varchar(30) DEFAULT NULL,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS hosts;

CREATE TABLE IF NOT EXISTS hosts (
	id SERIAL,
	hostname varchar(100) DEFAULT NULL,
	main_service varchar(45) DEFAULT NULL,
	image_type varchar (40) DEFAULT NULL,
	service_type varchar (10) DEFAULT NULL,
	environment varchar (10) DEFAULT NULL,
	owner_email varchar(55) DEFAULT NULL,
	team_id integer DEFAULT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (team_id) REFERENCES teams(id)
);

DROP TABLE IF EXISTS services;

