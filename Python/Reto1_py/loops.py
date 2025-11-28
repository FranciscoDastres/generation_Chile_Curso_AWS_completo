# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit)

fruits  = [
    {"name":"apple","price":10.99,"quantity":3},
    {"name":"banana","price":5.00,"quantity":10},
    {"name":"cherry","price":.99,"quantity":9}
]

total_sales = 0.0

for fruit in fruits:
    total_fruit=fruit["price"] * fruit["quantity"]
    total_sales=total_fruit

print(f"Tu total de venta es : {total_sales}")

frutas = []
 
while True:
    nombre = input("Ingresa el nombre de la fruta que deseas agregar: ")
 
    if nombre == "salir": # salir cuando el usuario ingrese 'salir'
        break
    precio = float(input(f"Ingresa el precio de {nombre}: "))
 
    fruta = {
        "nombre" :nombre,
        "precio" : precio
    }
    frutas.append(fruta)
    print(f"Ingresando la fruta: {nombre} con el precio de {precio}")
 
print("Frutas ingresadas:", frutas)