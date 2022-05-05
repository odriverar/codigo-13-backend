DELIMITER $$

CREATE PROCEDURE sp_listar_alumnos()
  BEGIN
    SELECT * FROM tbl_alumno;
  END
$$

DELIMITER ;

CALL listar_alumnos();

-- Procedmiento para matricular a un alumno
--  Registrar la tabla TBL_MATRICULA
--  Registrar la tabla TBL_MATRICULA_CURSO con todos los cursos
DELIMITER //
CREATE PROCEDURE sp_matricular_alumno(IN alu_id INT, IN niv_id INT, IN mod_id INT)
  BEGIN
    -- Variables
    DECLARE curId INT;
    DECLARE matId INT;
    DECLARE totalCursos INT;

    SET curId = 1;
    SET matId = 0;

    -- Insertar datos en la tabla matricula
    INSERT INTO tbl_matricula(alumno_id, nivel_id, modulo_id)
    VALUES(alu_id, niv_id, mod_id);

    SELECT MAX(matricula_id) INTO matId FROM tbl_matricula;
    SELECT COUNT(*) FROM tbl_curso;
    
    WHILE curId <= totalCursos DO
        INSERT INTO tbl_matricula_curso(matricula_id, curso_id)
        VALUES (matId, curId);

        SET curId = curId + 1;
    END WHILE;
  END
//

DELIMITER ;
CALL sp_matricular_alumno(5, 1, 1);