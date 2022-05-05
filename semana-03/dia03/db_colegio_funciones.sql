-- FUNCIONES
DELIMITER $$
CREATE FUNCTION fn_contar_cursos()
    RETURNS INT UNSIGNED
BEGIN
    DECLARE total INT UNSIGNED;

    SELECT count(*) INTO total FROM tbl_curso;

    RETURN total;
END
$$

DELIMITER ;
SELECT fn_contar_cursos();