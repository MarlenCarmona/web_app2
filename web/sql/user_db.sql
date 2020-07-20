CREATE DATABASE user_db;
USE user_db;

CREATE TABLE usuarios(
    id_usuario int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(100) NOT NULL,
    primer_apellido varchar(100) NOT NULL,
    segundo_apellido varchar(100) NOT NULL,
    matricula char(10) NOT NULL,
    edad char(2) NOT NULL,
    fecha_nac varchar(15) NOT NULL,
    genero varchar(10) NOT NULL,
    estado varchar(100) NOT NULL
) ENGINE= InnoDB DEFAULT CHARSET=latin1;

INSERT INTO usuarios(nombre,primer_apellido,segundo_apellido,matricula,edad,fecha_nac,genero,estado)
VALUES
('Marlen','Carmona','Lopez','1718110379','20','05-10-00','Mujer','Hidalgo'),
('America','Cruz','Alvarez','1718110380','20','15-01-00','Mujer','Hidalgo');

CREATE USER 'user_m'@'localhost' IDENTIFIED By 'User_bd';
GRANT ALL PRIVILEGES ON user_db. *TO 'user_m'@'localhost';
FLUSH PRIVILEGES;
