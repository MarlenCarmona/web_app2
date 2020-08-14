DROP DATABASE IF EXISTS user_db;
CREATE DATABASE user_db;
USE user_db;

CREATE TABLE usuarios(
    id_usuario int(11) NOT NULL  PRIMARY KEY,
    nombre varchar(100) NOT NULL,
    primer_apellido varchar(100) NOT NULL,
    segundo_apellido varchar(100) NOT NULL,
    edad char(2) NOT NULL,
    fecha_nac varchar(15) NOT NULL,
    genero varchar(10) NOT NULL,
    estado varchar(100) NOT NULL
) ENGINE= InnoDB DEFAULT CHARSET=latin1;

INSERT INTO usuarios(id_usuario,nombre,primer_apellido,segundo_apellido,edad,fecha_nac,genero,estado)
VALUES
('1718110379','Marlen','Carmona','Lopez','20','05-10-00','Mujer','Hidalgo'),
('1718110388','America','Cruz','Alvarez','20','15-01-00','Mujer','Hidalgo');

/*CREATE USER 'user_m'@'localhost' IDENTIFIED By 'User_bd';
GRANT ALL PRIVILEGES ON user_db. *TO 'user_m'@'localhost';
FLUSH PRIVILEGES;*/
