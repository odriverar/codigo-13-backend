INSERT INTO tbl_matricula(matricula_fecha_registro, alumno_id, nivel_id, modulo_id)
SELECT CURRENT_TIMESTAMP, 
       alumno_id,
       (SELECT nivel_id FROM tbl_nivel LIMIT 1),
       (SELECT modulo_id FROM tbl_modulo LIMIT 1)
  FROM tbl_alumno;

SELECT * FROM tbl_matricula;
