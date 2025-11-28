def saludo(nombre, edad):
    total_dias = calculo_anios_por_edad(edad)
    print(f"Hola, {nombre}! que bueno tenerte de regreso, han pasado {total_dias} desde que naciste")
 
def calculo_anios_por_edad(edad):
    dias_anio = 365
    dias_totales = dias_anio * edad
    return dias_totales
 
saludo("Gabriel", 42)