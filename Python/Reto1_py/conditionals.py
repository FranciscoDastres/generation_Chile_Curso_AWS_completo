MAYOR_EDAD = 18

edad = input("Ingrese su edad: ")

if int(edad) > MAYOR_EDAD: # si es verdadero
    print("Eres mayor de edad")
elif int(edad) == MAYOR_EDAD:
    print("Eres mayor de edad, tienes exactamente 18 años")
else:
    print("Eres menor de edad")

def definit_etapa_vida(edad):
    if (edad) < 12:
            print("Eres un niño")
    elif (edad) < 18:
            print("Eres un adulto")
    elif (edad) < 25:
            print("Eres un adulto joven")
    elif (edad) < 60:
            print("Eres un adulto mayor")

