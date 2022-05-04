CREATE TABLE IF NOT EXISTS alumno (
  id int(11) NOT NULL AUTO_INCREMENT,
  nombres varchar(100) NOT NULL,
  apellidos varchar(100) NOT NULL,
  email varchar(100) NOT NULL,
  pais varchar(100) DEFAULT 'Perú',
  nota int(11) DEFAULT '0',
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS alumno_nota(
    id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    alumno_id int(11) NOT NULL,
    curso VARCHAR(100) NOT NULL,
    nota INT(11) DEFAULT 0,
    FOREIGN KEY (alumno_id) REFERENCES alumno(id)
);

SELECT * FROM alumno;

---- Poblando tabla notas


INSERT INTO alumno_nota (alumno_id, curso, nota)
VALUES 
(1, 'HTML Y CSS', 13),
(1, 'JAVASCRIPT', 16),
(1, 'REACT', 18),
(1, 'PYTHON', 20),
(1, 'MYSQL', 11);

INSERT INTO alumno_nota (alumno_id, curso, nota)
VALUES 
(2, 'HTML Y CSS', 13),
(2, 'JAVASCRIPT', 15),
(2, 'REACT', 18),
(2, 'PYTHON', 20),
(2, 'MYSQL', 11);

INSERT INTO alumno_nota (alumno_id, curso, nota)
VALUES 
(3, 'HTML Y CSS', 13),
(3, 'JAVASCRIPT', 15),
(3, 'REACT', 18),
(3, 'PYTHON', 20),
(3, 'MYSQL', 11);

SELECT * FROM alumno_nota;