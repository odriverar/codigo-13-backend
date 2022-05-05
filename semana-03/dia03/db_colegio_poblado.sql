-- Poblado de datos
-- ALUMNO
INSERT INTO tbl_alumno(alumno_nombre, alumno_email, alumno_celular, alumno_github)
VALUES
('David Rivera Robles', 'odriverar@gmail.com', '987762000', 'https://github.com/odriverar'),
('Jose Ramirez León', 'joseramirez@gmail.com', '987762001', 'https://github.com/jramirezl'),
('Juan Fernandez Arce', 'juanfernandez@gmail.com', '987762002', 'https://github.com/jfernandeza'),
('Lia Gomez Chavez', 'lia_gomez@gmail.com', '987762003', 'https://github.com/lgomezc'),
('Yenny Huaman Toribio', 'yennyhuaman@gmail.com', '987762004', 'https://github.com/yhuamant');

-- CURSO
INSERT INTO tbl_curso (curso_nombre)
VALUES
('HTML Y CSS'),
('JAVASCRIPT'),
('REACT.JS'),
('PYTHON'),
('MYSQL'),
('FLASK');

-- EVALUACIONES
INSERT INTO tbl_evaluacion (evaluacion_nombre)
VALUES('PROYECTO CURSO');

-- MODULO
INSERT INTO tbl_modulo(modulo_nombre, modulo_fecha_inicio, modulo_nro_sesiones)
VALUES
('FRONTEND', '2022-01-01', 15),
('BACKEND', '2022-03-01', 15);

-- NIVEL
INSERT INTO tbl_nivel(nivel_nombre)
VALUES
('BASICO'),('AVANZADO');