* Que es ? 
 # Es un servicio que permite lanzar y administrar múltiples tipos de instnacias EC2 en una sola solicitud
 # Puede combinar  On demand , Spot
 # Su objetivo es optimizar costo y disponibilidad

* PAra que sirve ?
 # Mezclar instancias Spot y On-Demand
 # Mantener capacidad deseada automáticamente
 # Optimizar precio en cargas variables
 # Mejorar resiliencia usando múltiples tipos de instancia

* Como funciona ?
 - Tu defines
 # Capacidad total deseada
 # Tipos de instancias permitidos
 # Regiones o AZ
 # Estategia de asignacion

 # EC2 Fleet selecciona automáticamente la mejor combinacion  disponible

 # | Tipo      | ¿Se interrumpe? | ¿Descuento? | Uso típico       |
 # | --------- | --------------- | ----------- | ---------------- |
 # | On-Demand | No              | No          | Flexible         |
 # | Reserved  | No              | Sí          | Base constante   |
 # | Spot      | Sí              | Mucho       | Picos tolerantes |

# Carga constante → Reservadas
# Carga variable/interrumpible → Spot
# Carga impredecible corta → On-Demand