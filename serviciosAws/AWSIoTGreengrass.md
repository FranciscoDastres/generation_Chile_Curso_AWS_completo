* Que es? 
 # Un servicio que permite ejecutar procesamiento local(edge computing) en dispositivos IoT((lo mas cerca posible donde se generan))
 # Permite correr efunciones Lambda y lógica sin conexión constante a internet
 # Extiende AWS al "Edge" (Permite ejecutar código localmente en dispositivos procesa datos antes de enviarlos a la nube)
 # Es como llevar AWS dentro del dispositivo

* Para que sirve?
 # Procesar datos localmente
 # Reducir latencia
 # Funcionnar sin conexión permanente
 # FIltrar datos antes de enviarlos a la nube
 # Ejecutar ML en el edge

* Ejemplos reales: 
 # Cámara de seguridad que analiza viudeo localmente
 # Fábrica que procesa datos en tiempo real sin depender de internet
 # Vehículo autónomo que toma desciciones locales
 # Sensores industriales que filtran datos anest de enviarlos a AWS 

* Como funciona? 
 # El dispositivo instala el Greengrass Core
 # Puede ejecutar:
  - AWS Lambda
  - Contenedores
  - Modelos de Machine Learning
 # Se sincroniza con AWS IoT Core
 # Cuando vuelve la conexión, envía datos pendientes
 # Permite comunicación local entre dispositivos   

* Diferencia entre IoT Core y Greengrass
 # IoT Core → Conecta dipositivos a la nube
 # IoT Greengrass → Procesa datos localmente en el dispositivo
 # IoT Core = nube
 # IoT Greengrass = edge

* Greengrass = AWS en el edge (procesamiento local) 

# Dipositivos que deben procesar datos localmente sin depender de la conexión constante
 * AWS IoT Greengrass

# Necesitas ejecutar funciones Lambda en dispositivos IoT
 * AWS IoT Greengrass

# Necesitas conectar millones de dispositivo a la nube
 * AWS IoT Core  