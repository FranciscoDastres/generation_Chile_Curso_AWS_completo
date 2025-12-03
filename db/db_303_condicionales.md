# Instruccion SELECT tiene clausulas principales que se pueden usar, aunque FROM es la unica obligatoria

# Condicion de búsqueda es una prueba lógica que se puede aplicar a una fila, La estructura usa 2 expresiones devalores y un operador, y comprueba la relacion entre 2 valores

# Operadores de Comparación en SQL

A continuación se presentan los operadores de comparación más comunes, junto con su descripción y ejemplos.

---

## Tabla de operadores

| Operador | Descripción | Ejemplo |
|---------|-------------|---------|
| `=` | Comprueba si los valores de dos operandos son iguales. | `(a = b)` → **falso** |
| `!=` | Comprueba si los valores de dos operandos NO son iguales. | `(a != b)` → **verdadero** |
| `<>` | Funciona igual que `!=`, verifica si los valores NO son iguales. | `(a <> b)` → **verdadero** |
| `>` | Comprueba si el valor del operando izquierdo es mayor que el derecho. | `(a > b)` → **falso** |
| `<` | Comprueba si el valor del operando izquierdo es menor que el derecho. | `(a < b)` → **verdadero** |

---

## Ejemplo práctico

Supongamos que:

- `a = 5`  
- `b = 10`

Aplicando los operadores:

- `a = b` → falso  
- `a != b` → verdadero  
- `a <> b` → verdadero  
- `a > b` → falso  
- `a < b` → verdadero  

---

# Operadores Lógicos en SQL

Los operadores lógicos permiten combinar condiciones o evaluar conjuntos de valores en consultas SQL.

---

## Tabla de operadores lógicos

| Operador | Descripción |
|----------|-------------|
| **ALL** | Devuelve **TRUE** si *todas* las comparaciones de un conjunto son verdaderas. |
| **AND** | Devuelve **TRUE** si *ambas* expresiones booleanas son verdaderas. |
| **ANY** | Devuelve **TRUE** si *cualquiera* de un conjunto de comparaciones es verdadera. |
| **BETWEEN** | Devuelve **TRUE** si el operando está dentro de un rango. |
| **EXISTS** | Devuelve **TRUE** si una subconsulta devuelve al menos una fila. |
| **IN** | Devuelve **TRUE** si el operando coincide con *alguno* de los valores de una lista. |
| **LIKE** | Devuelve **TRUE** si el operando coincide con un patrón. |
| **OR** | Devuelve **TRUE** si *cualquiera* de las expresiones booleanas es verdadera. |
| **SOME** | Igual que **ANY**: TRUE si alguna comparación es verdadera. |
| **NOT** | Invierte el valor lógico de cualquiera de los operadores anteriores. |

---

## Ejemplos rápidos

```sql
-- AND
SELECT * FROM productos
WHERE precio > 10 AND stock > 0;

-- OR
SELECT * FROM usuarios
WHERE ciudad = 'Santiago' OR ciudad = 'Valparaíso';

-- BETWEEN
SELECT * FROM ventas
WHERE fecha BETWEEN '2024-01-01' AND '2024-12-31';

-- IN
SELECT * FROM empleados
WHERE cargo IN ('Manager', 'Developer', 'Analyst');

-- LIKE
SELECT * FROM clientes
WHERE nombre LIKE 'Fran%';

-- EXISTS
SELECT * FROM categorias c
WHERE EXISTS (SELECT 1 FROM productos p WHERE p.categoria_id = c.id);
