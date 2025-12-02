-- forma de agregar un valor a una columna por tabla en sql -- 
INSERT INTO tablename (col_1,col_2,col_3,col_4,col_5)
VALUES ("val_1","val_2","val_3","val_4","val_5")
-- describe Es un comando que sirve para ver la estructura de una tabla en la base de datos.-- 
DESCRIBE tablename
-- null--
INSERT INTO tablename (col_1) VALUES (null);