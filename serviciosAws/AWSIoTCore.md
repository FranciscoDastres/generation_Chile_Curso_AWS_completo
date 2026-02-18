* Que es ?
 # Es un servicio que permite conectar dispositivos físicos(IoT) a la nube de AWS de forma segura y escalable
 # IoT = Internet of Things(sensores, cámaras, medidores, dispositivos industriales,etc)
 # Permite que dispositivos envíen y reciban datos de forma segura
 # Escala a millones de dispositivos
 # Es el puente entre dispositivos físicos y la nube
* Que hace?
 # Permite que dispositivos:
  - Envién datos a la nube
  - Reciban comandos desde la nube
  - Se autentiquen de forma segura
  - Integren datos con otros servicios AWS

* Para que sirve:
 # Conectar sensores
 # Recibir telemetría ( proceso de recopilar datos auomaticamente desde dispositivos o sistemas remotos y enviarlos a otro lugar para monitoreo y analisis)
 # Enviar comandos a dispositivos
 # Procesar datos en tiempo real
 # Integrar dispositivos con otros servicios AWS

* Ejemplos reales:
 # Sensores de temperatura enviando datos cada minuto
 # Dispositivos industriales reportando métricas
 # Smart home (luce, cámaras, etc) 
* Cómo funciona?
 # 1 El dispositivo se conecta usando protocolos como:
  - MQTT (Protocolo ligero y optimizado para dispositivos pequeños y redes inestables)
  - HTTPS (Protocolo estándar para la web, pero cifrado)
  - WebSockets (Permite comunicación bidireccional en tiempo real entre cliente y servidor)
 # 2 Iot Core recibe los mensajes
 # 3 Puede enviarlos a: 
  - Lambda
  - DynamoDB
  - S3
  - Kinesis
  - SNS

* Componentes principales
 # Device Gateway: Permite conexión entre dispositivos
 # Message Broker: Recibe y enruta mensajes
 # Rules Engine: Define qué hacer con los datos

* Características importantes
 # Autenticación por certificados
 # Escalable a millones de dispositivos
 # Integración con casi todos los servicios AWS
 # Seguridad a nivel de dispositivo
 # Soporte comunicación bidireccional

* Diferencia con otros servicios
 # IoT Core → Conecta dispositivos físicos
 # API Gateway → Conectaa aplicaciones web/móviles
 # Kinesis → Streaming de datos
 # Timestream → Base de datos para métricas IoT

* IoT Core = conecta dispositivos físicos de forma segura

# Necesitas conectar millones de dispositivos que envían telemetría
 - AWS IoT Core

# Sensores envían datos cada segundo y quieres almacenarlos como series temporales
 - AWS IoT Core + Amazon Time Stream

# Necesitas procesar datos en tiempo real de dispositivos
 - IoT Core + Lambda 