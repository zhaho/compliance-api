--DROP TABLE IF EXISTS teams;

CREATE TABLE IF NOT EXISTS teams (
	id SERIAL,
	teamname varchar(50) DEFAULT NULL,
	when_changed varchar(30) DEFAULT NULL,
	when_created varchar(30) DEFAULT NULL,
	PRIMARY KEY (id)
);

--DROP TABLE IF EXISTS hosts;

CREATE TABLE IF NOT EXISTS hosts (
	id SERIAL,
	hostname varchar(100) DEFAULT NULL,
	main_service varchar(45) DEFAULT NULL,
	image_type varchar (40) DEFAULT NULL,
	service_type varchar (10) DEFAULT NULL,
	environment varchar (10) DEFAULT NULL,
	owner_email varchar(55) DEFAULT NULL,
	--host_location varchar(55) DEFAULT NULL,
	--backup_type varchar(55) DEFAULT NULL,
	team_id integer DEFAULT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (team_id) REFERENCES teams(id)
);

DROP TABLE IF EXISTS exporters;

CREATE TABLE IF NOT EXISTS exporters (
	id SERIAL,
	exportername varchar(40) DEFAULT NULL,
	port INT DEFAULT NULL,
	host_id INT DEFAULT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (host_id) REFERENCES hosts(id)
);

CREATE TABLE IF NOT EXISTS locations (
	id SERIAL,
	locationname varchar(40) DEFAULT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS environments (
	id SERIAL,
	environmentname varchar(40) DEFAULT NULL,
	PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS backup_types (
	id SERIAL,
	backup_name varchar(40) DEFAULT NULL,
	PRIMARY KEY (id)
);
	
CREATE TABLE IF NOT EXISTS api_users (
    user_id SERIAL,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    api_key VARCHAR(64) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    is_active BOOLEAN DEFAULT true,
	PRIMARY KEY (id)
);