# 🧠 Reto 1 --- Mini Ecommerce BI

Variables • Listas • Tuplas • Diccionarios\
+ Flujo completo GitHub (Fork → Clone → Push → Pull Request)\
**Sin condicionales ni loops**

------------------------------------------------------------------------

## 📌 Introducción

Bienvenido al **Reto 1** del curso.\
En este proyecto aplicarás TODO lo que hemos visto hasta ahora:

-   Variables\
-   Tuplas\
-   Listas\
-   Diccionarios\
-   Navegación de estructuras anidadas\
-   VS Code\
-   Flujo profesional con GitHub:\
    **Fork → Clone → Editar → Commit → Push → Pull Request**

Este reto simula un escenario real de negocio usando Python.

------------------------------------------------------------------------

# 🏪 Caso de negocio: *TechieStore*

Bootcamp Institute está apoyando a una tienda online llamada
**TechieStore**.\
La tienda quiere un *reporte rápido* que muestre información básica de
sus productos, precios y ventas.

Tu objetivo es crear un archivo en Python que produzca este reporte
**solo usando lo que sabemos hasta ahora**.

📌 **NO debes usar:**\
❌ condicionales (`if`)\
❌ bucles (`for`, `while`)\
❌ funciones avanzadas

Lo hacemos así a propósito para que domines a fondo las estructuras
básicas.

------------------------------------------------------------------------

# 📦 Datos iniciales (copia en tu archivo)

Copia este bloque dentro de tu archivo `reto_ecommerce.py`:

``` python
productos = [
    {"id": 1, "nombre": "Laptop Pro 14", "categoria": "Computo", "precio": 25000, "descuento": 0.10, "stock": 5},
    {"id": 2, "nombre": "Mouse Gamer X", "categoria": "Accesorios", "precio": 1200, "descuento": 0.15, "stock": 20},
    {"id": 3, "nombre": "Teclado Mecánico K1", "categoria": "Accesorios", "precio": 2200, "descuento": 0.05, "stock": 10},
    {"id": 4, "nombre": "Monitor 27'' 4K", "categoria": "Computo", "precio": 8000, "descuento": 0.20, "stock": 7},
    {"id": 5, "nombre": "Audífonos Bluetooth Z", "categoria": "Audio", "precio": 1500, "descuento": 0.0, "stock": 15},
]

ventas = [
    {"venta_id": 101, "producto_id": 1, "cantidad": 1, "cliente": "Ana"},
    {"venta_id": 102, "producto_id": 2, "cantidad": 2, "cliente": "Luis"},
    {"venta_id": 103, "producto_id": 4, "cantidad": 1, "cliente": "Sofía"},
    {"venta_id": 104, "producto_id": 2, "cantidad": 1, "cliente": "Carlos"},
    {"venta_id": 105, "producto_id": 5, "cantidad": 3, "cliente": "Ana"},
]

tienda_info = ("TechieStore", "Santiago", 2025)
```

------------------------------------------------------------------------

# 🎯 Objetivos del Reto

Completa las siguientes tareas dentro de `reto_ecommerce.py`:

------------------------------------------------------------------------

## ✅ 1. Mensaje de bienvenida

Usa la tupla `tienda_info` para imprimir:

    Bienvenido a TechieStore en Santiago (2025)

------------------------------------------------------------------------

## ✅ 2. Mostrar cuántos productos existen

Usa `len(productos)` para mostrar:

    Total de productos: 5

------------------------------------------------------------------------

## ✅ 3. Precio final con descuento (sin loops)

Para cada producto (a mano, uno por uno), calcula:

    precio_final = precio - (precio * descuento)

Y muestra:

    Laptop Pro 14 → $22500.0
    Mouse Gamer X → $1020.0
    ...

------------------------------------------------------------------------

## ✅ 4. Total de cada venta (sin loops)

Para cada venta:

1.  Identifica el producto correspondiente\
2.  Usa el precio final calculado\
3.  Multiplica por la cantidad

Ejemplo para la venta 101:

    Venta 101: Ana compró 1 Laptop Pro 14 y pagó 22500.0

------------------------------------------------------------------------

## ✅ 5. Ingreso total de la tienda

Suma manualmente:

    ingreso_total = total_venta_101 + total_venta_102 + ...

Luego imprime:

    Ingreso total: XXXXX

------------------------------------------------------------------------

# 📄 Entrega Final

El archivo debe llamarse:

    reto_ecommerce.py

Y debe estar en la raíz de tu repositorio.

------------------------------------------------------------------------

# 🔵 🚀 Flujo completo de GitHub

### (Fork → Clone → Crear archivo → Commit → Push → Pull Request)

------------------------------------------------------------------------

## 🧰 1. Haz **Fork** del repositorio del instructor

1.  Ve al repositorio original del profesor.\
2.  Da clic en el botón **Fork**.\
3.  Se creará una copia en tu GitHub personal.

------------------------------------------------------------------------

## 💻 2. Clona tu Fork a tu computadora

``` bash
git clone https://github.com/TU_USUARIO/NOMBRE_DEL_REPO.git
cd NOMBRE_DEL_REPO
```

------------------------------------------------------------------------

## ✏️ 3. Crea tu archivo del reto

``` bash
code reto_ecommerce.py
```

------------------------------------------------------------------------

## 💾 4. Guarda tus cambios en Git

``` bash
git add reto_ecommerce.py
git commit -m "Agrego mi solución del Reto 1"
```

------------------------------------------------------------------------

## ⬆️ 5. Envía tus cambios a GitHub

``` bash
git push origin main
```

------------------------------------------------------------------------

## 🔀 6. Crea un Pull Request al repositorio del profesor

1.  Abre tu fork en GitHub.\
2.  Haz clic en **Compare & Pull Request**.\
3.  Escribe un mensaje como:

```{=html}
<!-- -->
```
    Entrego mi solución del Reto 1 – Mini Ecommerce BI

4.  Envía el Pull Request.

------------------------------------------------------------------------

# 🎉 ¡Listo!

Este reto te ayudará a:

-   Dominar variables y estructuras de datos\
-   Usar VS Code como un entorno profesional\
-   Trabajar con GitHub como en una empresa real\
-   Conectar Python con un caso de negocio real
