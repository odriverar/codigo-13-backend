DELIMITER ;
SELECT * FROM tbl_matricula_curso;

CREATE VIEW vw_matricula_notas AS
    SELECT tm.matricula_fecha_registro AS fecha,
           ta.alumno_nombre AS alumno,
           tc.curso_nombre AS curso,
           mc.curso_nota AS nota
      FROM tbl_matricula_curso mc inner join tbl_matricula tm
        ON tm.matricula_id = mc.matricula_id INNER JOIN tbl_alumno ta
        ON ta.alumno_id = tm.alumno_id INNER JOIN tbl_curso tc
        ON tc.curso_id = mc.curso_id;

SELECT * FROM vw_matricula_notas;