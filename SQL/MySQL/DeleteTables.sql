-- BORRAR TABLAS

-- SELECCIONAR BASE DE DATOS
USE `voto-vision`;

-- ESTABLECER JUEGO DE CARACTERES
SET NAMES utf8mb4;

-- VER VARIABLE GLOBAL
SHOW VARIABLES LIKE "SQL_SAFE_UPDATES";
-- DESHABILITAR ACTUALIZACIÓN SEGURA
SET SQL_SAFE_UPDATES = 0;
-- DESACTIVAR VERIFICACIONES DE CLAVES FORÁNEAS
SET FOREIGN_KEY_CHECKS = 0;

-- ELIMINAR TABLA
DELETE FROM `APLICACION_MODELO`;
-- ELIMINAR TODOS LOS REGISTROS
TRUNCATE TABLE `APLICACION_MODELO`;
-- REINICIAR CONTADOR DE ID
ALTER TABLE `APLICACION_MODELO` AUTO_INCREMENT = 1;
-- SELECCIONAR TABLA
SELECT * FROM `APLICACION_MODELO`;

-- ELIMINAR TABLA
DELETE FROM `auth_user`;
-- ELIMINAR TODOS LOS REGISTROS
TRUNCATE TABLE `auth_user`;
-- REINICIAR CONTADOR DE ID
ALTER TABLE `auth_user` AUTO_INCREMENT = 1;
-- SELECCIONAR TABLA
SELECT * FROM `auth_user`;

-- ACTIVAR VERIFICACIONES DE CLAVES FORÁNEAS
SET FOREIGN_KEY_CHECKS = 1;
-- HABILITAR ACTUALIZACIÓN SEGURA
SET SQL_SAFE_UPDATES = 1;
-- VER VARIABLE GLOBAL
SHOW VARIABLES LIKE "SQL_SAFE_UPDATES";