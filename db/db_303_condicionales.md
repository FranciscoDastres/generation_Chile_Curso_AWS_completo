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

# Prioridad de Operadores en SQL

El orden de precedencia determina qué operadores se evalúan primero en una expresión.  
A continuación se muestra la jerarquía desde **mayor prioridad (1)** hasta **menor prioridad (9)**.

---

## Tabla de prioridad de operadores

| Nivel | Operadores |
|-------|------------|
| **1** | `+` (Positivo), `-` (Negativo), `~` (NOT bit a bit) |
| **2** | `*` (Multiplicación), `/` (División), `%` (Módulo) |
| **3** | `+` (Suma), `+` (Concatenación), `-` (Resta) |
| **4** | `=`, `>`, `<`, `>=`, `<=`, `<>`, `!=`, `!>`, `!<` *(Operadores de comparación)* |
| **5** | `^` (OR exclusivo bit a bit), `&` (AND bit a bit), `|` (OR bit a bit) |
| **6** | `NOT` |
| **7** | `AND` |
| **8** | `ALL`, `ANY`, `BETWEEN`, `IN`, `LIKE`, `OR`, `SOME` |
| **9** | `=` (Asignación) |

---

## Ejemplo ilustrativo

```sql
-- Ejemplo demostrando la prioridad
SELECT 5 + 10 * 2 > 20 AND 3 IN (1, 2, 3);

-- Se evalúa así:
-- 10 * 2        -> nivel 2
-- 5 + 20        -> nivel 3
-- 25 > 20       -> nivel 4
-- 3 IN (...)    -> nivel 8
-- resultado1 AND resultado2 -> nivel 7

# Uso de Alias en SQL

Los **alias** permiten asignar un nombre temporal a columnas o tablas dentro de una consulta SQL.  
Se utilizan principalmente para:

- Hacer que los resultados sean más legibles.
- Acortar nombres largos de tablas.
- Facilitar el trabajo con subconsultas.
- Mejorar la claridad cuando se usan funciones o cálculos.

Los alias **no modifican** la estructura real de la base de datos: solo existen mientras se ejecuta la consulta.

---

## Alias para columnas

Se usan para renombrar una columna en el resultado.  
Puedes usar `AS` o simplemente un espacio.

### Ejemplo:

```sql
SELECT nombre AS nombre_cliente,
       edad AS años
FROM usuarios;

SELECT nombre nombre_cliente,
       edad años
FROM usuarios;

SELECT u.nombre, o.total
FROM usuarios AS u
JOIN ordenes AS o
    ON u.id = o.usuario_id;

SELECT u.nombre, o.total
FROM usuarios u
JOIN ordenes o
    ON u.id = o.usuario_id;

SELECT precio * 0.19 AS iva,
       precio + (precio * 0.19) AS precio_total
FROM productos;

SELECT p.nombre, ventas_totales.total
FROM productos p
JOIN (
    SELECT producto_id, SUM(cantidad) AS total
    FROM ventas
    GROUP BY producto_id
) ventas_totales
ON p.id = ventas_totales.producto_id;

# Pruebas con valores NULL en SQL

Cuando se trabajan expresiones lógicas en SQL, el valor **NULL** representa “desconocido”.  
Esto provoca resultados especiales cuando se combina con operadores lógicos como `AND` y `OR`.

---

## Resultados de operaciones lógicas con NULL

| Expresión 1 | Expresión 2 | Resultado con **AND** | Resultado con **OR** |
|-------------|-------------|------------------------|-----------------------|
| TRUE        | NULL        | NULL                   | TRUE                  |
| FALSE       | NULL        | FALSE                  | NULL                  |
| NULL        | NULL        | NULL                   | NULL                  |
| UNKNOWN     | FALSE       | FALSE                  | UNKNOWN               |

---

## Reglas importantes sobre NULL

- **No se puede usar `=`, `<`, `<>`, `!=` ni ningún operador de comparación para evaluar NULL.**  
- Para evaluar NULL debes usar:  
  - `IS NULL`  
  - `IS NOT NULL`

### Ejemplo:

```sql
SELECT * FROM empleados
WHERE fecha_retiro IS NULL;
