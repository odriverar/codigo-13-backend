-- TRIGGER -- DISPARADORES
SELECT alumno_nombre,
       CONCAT(REPLACE(LOWER(alumno_nombre), ' ', ''), '@tecsup.edu.pe')
FROM tbl_alumno;

DELIMITER //

CREATE TRIGGER tg_correo_alumno
BEFORE INSERT 
ON tbl_alumno FOR EACH ROW
    BEGIN
        SET NEW.alumno_email = CONCAT(REPLACE(LOWER(NEW.alumno_nombre), ' ', ''), '@tecsup.edu.pe');
    END;
