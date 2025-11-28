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
## 1. Mensaje de bienvenida

print(f"Bienvenido a {tienda_info[0]} en {tienda_info[1]} ({tienda_info[2]})")
## 2. Mostrar cuántos productos existen

cantidad_total_productos =(len(productos))
print(f"Total de productos: {cantidad_total_productos}")

## 3. Precio final con descuento ( sin loops)

precio_final_1 = productos[0]["precio"] - (productos[0]["precio"] * productos[0]["descuento"])
precio_final_2 = productos[1]["precio"] - (productos[1]["precio"] * productos[1]["descuento"])
precio_final_3 = productos[2]["precio"] - (productos[2]["precio"] * productos[2]["descuento"])
precio_final_4 = productos[3]["precio"] - (productos[3]["precio"] * productos[3]["descuento"])
precio_final_5 = productos[4]["precio"] - (productos[4]["precio"] * productos[4]["descuento"])

print(f'{productos[0]["nombre"]} → ${precio_final_1}')
print(f'{productos[1]["nombre"]} → ${precio_final_2}')
print(f'{productos[2]["nombre"]} → ${precio_final_3}')
print(f'{productos[3]["nombre"]} → ${precio_final_4}')
print(f'{productos[4]["nombre"]} → ${precio_final_5}')

## 4. Total de cada venta (sin loops)

total_101 = precio_final_1 * ventas[0]["cantidad"]
total_102 = precio_final_2 * ventas[1]["cantidad"]
total_103 = precio_final_4 * ventas[2]["cantidad"]
total_104 = precio_final_2 * ventas[3]["cantidad"]
total_105 = precio_final_5 * ventas[4]["cantidad"]

print(f'Venta 101: {ventas[0]["cliente"]} compró {ventas[0]["cantidad"]} {productos[0]["nombre"]} y pagó {total_101}')
print(f'Venta 102: {ventas[1]["cliente"]} compró {ventas[1]["cantidad"]} {productos[1]["nombre"]} y pagó {total_102}')
print(f'Venta 103: {ventas[2]["cliente"]} compró {ventas[2]["cantidad"]} {productos[3]["nombre"]} y pagó {total_103}')
print(f'Venta 104: {ventas[3]["cliente"]} compró {ventas[3]["cantidad"]} {productos[1]["nombre"]} y pagó {total_104}')
print(f'Venta 105: {ventas[4]["cliente"]} compró {ventas[4]["cantidad"]} {productos[4]["nombre"]} y pagó {total_105}')

ingreso_total = total_101 + total_102 + total_103 + total_104 + total_105
print(f"El ingreso total es : {ingreso_total}")