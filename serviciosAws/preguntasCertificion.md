## ¿Cómo cobra AWS por el uso de AWS Lambda una vez excedido el nivel gratuito? (Seleccione DOS).
* Segun el tiempo que la funcion Lamba esta en ejecucion
* Segun la cantidad de solicitudes realizadas para una determinada  funcion Lambda

## ¿Qué servicio de AWS les permite a los clientes comprar capacidad sin usar de Amazon EC2 a una tarifa con descuento frecuente?
* Spot Instances Con las Spot Instances, puede acceder a la capacidad sin usar de EC2. Las Spot Instances pueden tener descuento.

## ¿Qué servicio de AWS se debe usar para implementar el cifrado en tránsito?
* AWS Certificate Manager(ACM) es un servicio que se usa para crear, almacenar y renovar certificados SSL/TLS, tanto publicos como privados, puede usar aACM para imeplementar el cifrado en transito y en reposo mediante un protocolo, como el de TLS

## Una empresa desea establecer una conexión coherente y privada desde el centro de datos en las instalaciones de la empresa a la nube de AWS.¿Qué servicio de AWS puede cumplir con estos requisitos?

* AWS Direct Conect: vincula red interna con una ubicacion de direct connect mediante un cable estandar de ethernet de fibra, un extremo se conecta al enrutador, el otro se conecta a un enrutador de direct connect es coherente y privado porque su empresa es el unico usuario del cable

## ¿Cuáles son los beneficios de utilizar la nube de AWS para empresas con clientes de muchos países del mundo? (Seleccione DOS).

* Las empresas pueden implementar aplicacione  en varias regiones de AWS para reducir la latencia
* Amazon CloudFront tiene varias ubicaciones perimetrales en todo el mundo para reducir la latencia

## Un equipo de desarrollo de aplicaciones necesita una solución que envíe una alerta a todo el equipo de desarrollo en caso de que una prueba de control de calidad falle en una aplicación. ¿Qué servicio de AWS debe usar el equipo de desarrollo de aplicaciones para cumplir con el requisito

* Amazon Simple Notificacion Service (Amazon SNS): es un servicio que se usa para enviar publicaciones a subs, puede enviar notificaciones como mensajes de texto push o correos electronicos a los subs de un tema sobre fallas en pruebas de control de calidad

## Cada departamento de una empresa tiene su propia cuenta independiente de AWS y su propio método de pago. La empresa necesita centralizar la gobernanza departamental y unificar los pagos. ¿Cómo puede la empresa alcanzar estos objetivos mediante el uso de servicios o funciones de AWS?

* Crear una organizacion en AWS organizations con todas las funciones habilitadas en uan cuenta, invitar a todas laas cuentas a unirse a la organizacion

## ¿Qué tareas son responsabilidad del cliente según el modelo de responsabilidad compartida de AWS? (Seleccione DOS).

* Configurar los usuarios de IAM segun el principio de minimo privilegio: define usaurios de IAM y politicas de acceso que se aplican a esos usuarios
* Configurar un bucket de Amazon s3 para permitir el acceso publico

## Una empresa tiene un servidor en las instalaciones basado en Linux con una base de datos Oracle que se ejecuta en él. La empresa desea migrar el servidor de base de datos para que se ejecute en una instancia de Amazon EC2 en AWS.¿Qué servicio debe utilizar la empresa para completar la migración?

* AWS Application Migration Service(AWS MGN): es una solucion automatizada de transporte y  cambio, esta siolucion peude migrar servidores fisicos y cualquier db o app que se ejecute en ellos a instancias de EC2 en AWS

## ¿Cuáles de las funcionalidades son características de Amazon S3? (Seleccione DOS).

* Almacen de objetos
* Sistema de almacenamiento duradero

## ¿Qué componentes de credenciales se necesitan para obtener acceso programático a una cuenta de AWS? (Seleccione DOS).

* ID de clave de acceso
* Clave de acceso Secreta

## Una empresa quiere crear una aplicación de aprendizaje para estudiantes. La aplicación de aprendizaje debe ofrecer a los alumnos la opción de elegir un botón para que se les lea el texto en voz alta.¿Qué servicio de machine learning de AWS cumplirá con este requisito?

* Amazon Plly es un servicio de MAchine learnign que convierte texto en voz este servicio permite leer textos en voz alta

## Un usuario implementa una instancia de base de datos de Amazon RDS en varias zonas de disponibilidad.¿Qué pilar del Marco de AWS Well-Architected involucra esta estrategia?

* Fiabilidad: incluye capacidad de una carga de trabajo para llevar a cabo la funcion prevista de forma correcta y coherente en el momento esperado. la implementacion de AMazon RDS en varias zonas de siponiblidad admite el objetivo de la fiabilidad porque reduce los puntos unicos de error

## ¿Cuáles son las ventajas de implementar una aplicación con instancias de Amazon EC2 en varias zonas de disponibilidad? (Seleccione DOS).

* Prevencion de un punto unico de error: eviuta tener un punto unico de error las zonas de dispo estan diseñadas para redundancia fisica y para ofrecer resistencia con un rendimiento ininterrumpido

* Aumento de la disponibildiad de la a app : las zonas de dispo estan diseñadas para redundancia fisica y para ofrecer resistencia con un rendimiento ininterrumpido

## ¿Cuál es el plan MÍNIMO de AWS Support que brinda soporte técnico a través de llamadas telefónicas?

* Business: Puede llamar o conversar con el soporte tenico mediante el plan Business support o el plan enterprise support, y el plan business support es esl plan minimo que brinda esta funcion

## ¿Qué servicio de AWS identifica los grupos de seguridad que permiten el acceso sin restricciones a los recursos de AWS de un usuario?

* TRusted Advisor verifica los grupos de seguridad en busca de reglas que permitan el acceso sin restricciones a un recurso, el acceso sin restricciones aumenta las oportuinidades de actividad malintencionada como pirateria ataques de denegacion de servicio o perdida de datos

## Una empresa necesita una conexión cifrada entre sus servidores en las instalaciones y AWS. La conexión debe utilizar la conexión a Internet existente en la empresa.¿Qué solución cumplirá con estos requisitos?

* AWS Site to Site VPN : crea una ruta de red CIFRADA  entre su red en las instalaciones y su red en la nube de AWS, esta conexion entre su red en las en las instalaciones y su red en la nube de AWS utiliza internet

## Una empresa aloja un sitio web estático desde un único bucket de Amazon S3. ¿Qué servicio de AWS conseguirá una menor latencia y una mayor velocidad de transferencia?

* Amazon Cloud Front: servicio web que agiliza disfritubcion de contenido web estatico y dinamico archivos html.css js y archivos de imagenes de usuario