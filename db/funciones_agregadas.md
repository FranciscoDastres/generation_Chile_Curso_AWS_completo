# 📚 Funciones Agregadas en MariaDB

Una **función agregada** toma muchas filas y devuelve **un solo valor** por cada grupo de filas. Se utilizan para obtener totales, promedios, máximos, mínimos, etc.

---

# 🧠 ¿Cómo funcionan? (Orden de ejecución relevante)

1. **FROM** – carga tablas y realiza JOINs
2. **WHERE** – filtra filas individuales
3. **GROUP BY** – crea grupos
4. **Funciones agregadas** – se calculan aquí
5. **HAVING** – filtra grupos ya agregados
6. **SELECT** – genera las columnas finales
7. **ORDER BY** – ordena
8. **LIMIT** – limita resultados

---

# 📌 Funciones agregadas más comunes en MariaDB

* `COUNT(*)` → cuenta todas las filas
* `COUNT(col)` → cuenta filas donde `col` **no es NULL**
* `COUNT(DISTINCT col)` → cuenta valores distintos
* `SUM(col)` → suma valores
* `AVG(col)` → promedio
* `MIN(col)` / `MAX(col)` → mínimo / máximo
* `GROUP_CONCAT(col SEPARATOR ',')` → concatena valores del grupo

---

# 📌 Comportamiento con NULL

* `SUM`, `AVG`, `MIN`, `MAX`, `COUNT(col)` **ignoran NULL**
* `COUNT(*)` cuenta todas las filas
* Si todos los valores son NULL: agregados devuelven NULL

---

# 📑 Ejemplos Prácticos

Usaremos la tabla `ventas`:

```sql
CREATE TABLE ventas (
  id INT PRIMARY KEY,
  vendedor VARCHAR(50),
  producto VARCHAR(50),
  cantidad INT,
  precio DECIMAL(10,2),
  fecha DATE
);
```

## ✔ Total de ventas por vendedor

```sql
SELECT vendedor,
       SUM(COALESCE(cantidad,0) * precio) AS total_ventas
FROM ventas
GROUP BY vendedor;
```

## ✔ Promedio de cantidades

```sql
SELECT vendedor, AVG(cantidad) AS promedio_cantidad
FROM ventas
GROUP BY vendedor;
```

## ✔ Conteos

```sql
SELECT vendedor,
       COUNT(*) AS filas_totales,
       COUNT(producto) AS filas_con_producto,
       COUNT(DISTINCT producto) AS productos_distintos
FROM ventas
GROUP BY vendedor;
```

## ✔ Filtrar grupos con HAVING

```sql
SELECT vendedor, SUM(cantidad * precio) AS total
FROM ventas
GROUP BY vendedor
HAVING SUM(cantidad * precio) > 50;
```

## ✔ Listar valores usando GROUP_CONCAT

```sql
SELECT vendedor,
       GROUP_CONCAT(DISTINCT producto ORDER BY producto SEPARATOR ', ') AS productos
FROM ventas
GROUP BY vendedor;
```

---

# 🎯 Agregados sin GROUP BY

```sql
SELECT COUNT(*) AS total_filas, SUM(precio) AS suma_precios
FROM ventas;
```

Devuelve un único valor global.

---

# 🔍 WHERE vs HAVING

* **WHERE** → filtra filas antes del agrupamiento
* **HAVING** → filtra después del agrupamiento (puede usar agregados)

Ejemplo:

```sql
SELECT vendedor, COUNT(*) AS cnt
FROM ventas
WHERE fecha >= '2025-11-01'
GROUP BY vendedor
HAVING COUNT(*) > 2;
```

---

# ⚠️ Agregados y JOINs — cuidado con duplicados

Un `JOIN` puede multiplicar filas y alterar SUM/COUNT. Posible solución:

```sql
SELECT v.vendedor,
       (SELECT SUM(cantidad * precio)
        FROM ventas v2
        WHERE v2.vendedor = v.vendedor) AS total
FROM (SELECT DISTINCT vendedor FROM ventas) v;
```

---

# 🪟 Funciones Ventana (complemento)

Si quieres sumar por vendedor sin perder filas:

```sql
SELECT id, vendedor, producto, cantidad,
       SUM(cantidad) OVER (PARTITION BY vendedor) AS suma_por_vendedor
FROM ventas;
```

---

# 🛠 Buenas Prácticas

* Filtra con `WHERE` antes del `GROUP BY`
* Índices en columnas usadas en `GROUP BY` o `JOIN`
* Evitar `SELECT *` combinado con `GROUP BY`
* Ajustar `group_concat_max_len` si concatenas grandes cantidades de datos

---

# 📦 Temas Avanzados

* `ROLLUP` → subtotales y totales
* `GROUPING SETS` / `CUBE` → múltiples agrupamientos
* Agregados JSON → `JSON_ARRAYAGG`, `JSON_OBJECTAGG`

---

Si quieres, puedo crear otro archivo `.md` para `SUBSTRING()`, `CONCAT()` o para cualquier otro tema de SQL.
