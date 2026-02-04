# Cuestionario AWS – Data y Cloud

---

## Pregunta 1

**Enunciado:** ¿Qué servicio de AWS utiliza machine learning para identificar la información confidencial que se almacena en los buckets de Amazon S3?

**Opciones:**

* a. AWS CodeArtifact
* b. Amazon Macie ✅
* c. AWS Cloud9
* d. Amazon Personalize

**Retroalimentación:** Macie es un servicio de seguridad de datos que detecta información confidencial utilizando machine learning y coincidencia de patrones para identificar información confidencial en buckets de S3.

**Respuesta correcta:** Amazon Macie

---

## Pregunta 2

**Enunciado:** Una empresa quiere asegurarse de que dos instancias de Amazon EC2 estén en centros de datos independientes con una latencia de comunicación mínima entre los centros de datos. ¿Cómo puede cumplir este requisito?

**Opciones:**

* a. Colocar las instancias en dos zonas de disponibilidad independientes dentro de la misma región ✅
* b. Colocar las instancias en dos regiones independientes conectadas mediante interconexión de VPC
* c. Colocar ambas instancias en un grupo de ubicación para ancho de banda dedicado
* d. Colocar una instancia en las instalaciones y la otra en una región de AWS, conectadas mediante VPN

**Retroalimentación:** El uso de dos zonas de disponibilidad en la misma región asegura baja latencia y protección ante fallas de una zona.

**Respuesta correcta:** Colocar las instancias en dos zonas de disponibilidad independientes dentro de la misma región

---

## Pregunta 3

**Enunciado:** ¿Qué servicio de base de datos de AWS proporciona almacenamiento de datos en memoria?

**Opciones:**

* a. Amazon DynamoDB
* b. Amazon ElastiCache ✅
* c. Amazon Timestream
* d. Amazon RDS

**Retroalimentación:** ElastiCache es un servicio completamente administrado de almacenamiento en caché en memoria para bases de datos.

**Respuesta correcta:** Amazon ElastiCache

---

## Pregunta 4

**Enunciado:** ¿Qué servicio de AWS puede utilizar una empresa para detectar un corte en los servidores de su sitio web y redirigir a los usuarios a servidores alternativos?

**Opciones:**

* a. Amazon Route 53 ✅
* b. AWS Trusted Advisor
* c. Amazon GuardDuty
* d. Amazon CloudFront

**Retroalimentación:** Route 53 permite el enrutamiento de conmutación por error mediante políticas de enrutamiento.

**Respuesta correcta:** Amazon Route 53

---

## Pregunta 5

**Enunciado:** Una empresa inicia una nueva aplicación en AWS. La aplicación se ejecutará en instancias EC2. Se necesitarán más instancias cuando aumente la carga. ¿Qué servicio de AWS puede iniciar automáticamente la cantidad de instancias necesarias?

**Opciones:**

* a. AWS Systems Manager
* b. Amazon EC2 Auto Scaling ✅
* c. Elastic Load Balancing (ELB)
* d. AWS App2Container (A2C)

**Retroalimentación:** Amazon EC2 Auto Scaling permite aumentar o reducir automáticamente el número de instancias según la carga.

**Respuesta correcta:** Amazon EC2 Auto Scaling

---

## Pregunta 6

**Enunciado:** Una empresa necesita ejecutar una aplicación en EC2 sin interrumpir la carga. ¿Qué opción de compra no requiere compromiso?

**Opciones:**

* a. Servidores dedicados
* b. Instancias bajo demanda ✅
* c. Instancias de spot
* d. Instancias reservadas

**Retroalimentación:** Las instancias bajo demanda no requieren compromiso previo y permiten flexibilidad total.

**Respuesta correcta:** Instancias bajo demanda

---

## Pregunta 7

**Enunciado:** Una empresa no posee centro de datos físico, pero necesita una solución de red que conecte laptops de empleados directamente a la nube de AWS. ¿Qué servicio cumple este requisito?

**Opciones:**

* a. AWS Snowball Edge
* b. AWS Client VPN ✅
* c. Amazon CloudFront
* d. AWS Outposts

**Retroalimentación:** Client VPN permite acceso seguro a recursos AWS desde cualquier ubicación mediante VPN administrada.

**Respuesta correcta:** AWS Client VPN

---

## Pregunta 8

**Enunciado:** Una empresa quiere alojar sus bases de datos relacionales en AWS con esquemas predefinidos. ¿Qué servicios podría utilizar? (Seleccione DOS)

**Opciones:**

* a. Amazon RDS ✅
* b. Amazon DynamoDB
* c. Amazon DocumentDB
* d. Amazon Aurora ✅
* e. Amazon Neptune

**Retroalimentación:** RDS y Aurora son servicios relacionales completamente administrados que soportan esquemas predefinidos.

**Respuestas correctas:** Amazon RDS, Amazon Aurora

---

## Pregunta 9

**Enunciado:** ¿Qué función puede proteger buckets de S3 contra sobreescrituras o eliminaciones accidentales?

**Opciones:**

* a. Control de versiones de un bucket ✅
* b. Encriptación del lado del servidor
* c. Políticas de ciclo de vida
* d. Puntos de acceso de S3

**Retroalimentación:** El control de versiones permite restaurar versiones anteriores de objetos eliminados o sobrescritos.

**Respuesta correcta:** Control de versiones de un bucket

---

## Pregunta 10

**Enunciado:** ¿Qué servicio puede generar un hallazgo cuando PII se almacena en un bucket de S3?

**Opciones:**

* a. AWS Trusted Advisor
* b. Amazon Inspector
* c. Amazon Macie ✅
* d. Amazon GuardDuty

**Retroalimentación:** Macie identifica PII en S3 mediante machine learning y coincidencia de patrones.

**Respuesta correcta:** Amazon Macie

---

## Pregunta 11

**Enunciado:** ¿Qué servicio de cómputo de AWS es serverless?

**Opciones:**

* a. Amazon RDS
* b. Amazon ECS
* c. Amazon EC2
* d. AWS Lambda ✅

**Retroalimentación:** Lambda es un servicio sin servidor, administrado por AWS.

**Respuesta correcta:** AWS Lambda

---

## Pregunta 12

**Enunciado:** Una instancia EC2 necesita acceder a S3 y DynamoDB. ¿Cuál es la solución más eficiente para delegar permisos?

**Opciones:**

* a. Crear un usuario de IAM y usar sus claves en CLI
* b. Crear un rol de IAM y adjuntarlo a la instancia ✅
* c. Crear un usuario de IAM y usar sus claves en la aplicación
* d. Crear un rol de IAM y adjuntarlo al usuario administrativo de IAM

**Retroalimentación:** Adjuntar un rol de IAM a la instancia es la mejor práctica para delegar permisos.

**Respuesta correcta:** Crear un rol de IAM y adjuntarlo a la instancia de EC2

---

## Pregunta 13

**Enunciado:** Después de seleccionar una reserva de servidor dedicado de EC2, ¿qué opción de precios ofrece el mayor descuento?

**Opciones:**

* a. Pago parcial anticipado
* b. Sin pago anticipado
* c. Pago por horas y bajo demanda
* d. Pago total anticipado ✅

**Retroalimentación:** Pago total anticipado ofrece el mayor descuento porque se paga todo por adelantado.

**Respuesta correcta:** Pago total anticipado

---

## Pregunta 14

**Enunciado:** ¿Qué beneficio de AWS permite implementar infraestructura en múltiples regiones con red de baja latencia y alta redundancia?

**Opciones:**

* a. Alcance global ✅
* b. Elasticidad
* c. Seguridad
* d. Economía de escala

**Retroalimentación:** Alcance global permite conectividad eficiente entre múltiples regiones.

**Respuesta correcta:** Alcance global

---

## Pregunta 15

**Enunciado:** Empresa con picos de ventas estacionales, difícil de predecir demanda de infraestructura. ¿Qué ventajas de AWS beneficiarían más? (Seleccione DOS)

**Opciones:**

* a. Modelo de responsabilidad compartida
* b. Precios de pago por uso ✅
* c. Elasticidad ✅
* d. Presencia global
* e. AWS Service Quotas

**Retroalimentación:** Pago por uso y elasticidad permiten ajustar recursos según demanda y pagar solo por lo usado.

**Respuestas correctas:** Elasticidad, Precios de pago por uso

---

## Pregunta 16

**Enunciado:** Empresa quiere crear aplicación de análisis de datos en Amazon Redshift. Necesita estimación de costos. ¿Qué herramienta usar?

**Opciones:**

* a. AWS Cost Explorer
* b. AWS Pricing Calculator ✅
* c. Savings Plans
* d. AWS Budgets

**Retroalimentación:** Pricing Calculator permite estimar costos antes de la implementación.

**Respuesta correcta:** AWS Pricing Calculator

---

## Pregunta 17

**Enunciado:** ¿Qué servicio se utiliza para monitorear instancias EC2 para uso de CPU y red?

**Opciones:**

* a. AWS Config
* b. Amazon Inspector
* c. AWS CloudTrail
* d. Amazon CloudWatch ✅

**Retroalimentación:** CloudWatch monitorea recursos y recopila métricas de CPU y red en tiempo real mediante agentes.

**Respuesta correcta:** Amazon CloudWatch
