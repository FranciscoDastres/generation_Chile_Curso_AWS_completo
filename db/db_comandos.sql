-- forma de agregar un valor a una columna por tabla en sql -- 
INSERT INTO tablename (col_1,col_2,col_3,col_4,col_5)
VALUES ("val_1","val_2","val_3","val_4","val_5")
-- describe Es un comando que sirve para ver la estructura de una tabla en la base de datos.-- 
DESCRIBE tablename
-- null--
INSERT INTO tablename (col_1) VALUES (null);

Select name, population from world.country WHERE NAME = "Chile"

Where = condition

Ltrim y Rtrim
lrim elimina espacios en blanco del extremo izquierdo de una cadena
lrim elimina espacios en blanco del extremo derecha de una cadena

trim solito elimina de ambos

SUBSTRING(cadena, inicio, largo)
Sirve para extraer una parte de un texto.
SELECT SUBSTRING('HolaMundo', 5);

Resultado: Mundo
(Empieza en la letra 5)


CONCAT(valor1, valor2, valor3, ...)
SELECT CONCAT('Hola', ' ', 'Mundo');

SELECT CONCAT(nombre, ' ', apellido) AS nombre_completo
FROM usuarios;

Concatenación de valores de columna y valores estáticos

SELECT repid, CONCAT(TRIM(LTRIM(Nombre)), ' ', TRIM(RTRIM(Nombre))) AS Nombre
FROM sgers

Esta consulta concatena el valor de la columna Nombre, eliminando los espacios finales e iniciales para generar un nombre limpio separado por comas.

Resultado
N°	Nombre
1	Elan, Kren
2	Lina, Morgan
3	Carl, Duncan
4	Neil, Paltrow
5	Glen, Parker
6	Will, Novak
7	Sean, Rourke
8	Troy, Avatar

Consulte la tabla country para arrojar un conjunto de registros basado en el siguiente requisito.

Escriba una consulta que arroje filas que tienen Micronesian/Caribbean como nombre en la columna de región. El resultado debe dividir la región como Micronesia y Caribbean en dos columnas separadas: una llamada Region Name 1 y una llamada Region Name 2.
SELECT Name, substring_index(Region, "/", 1) as "Region Name 1",substring_index(region, "/", -1) as "Region Name 2" FROM world.country WHERE Region = "Micronesia/Caribbean";

