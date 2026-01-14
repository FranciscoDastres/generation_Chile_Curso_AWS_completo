# 📘 Evaluación AWS – 65 Preguntas Completas

> **Fecha**: 7 de enero de 2026  
> **Tiempo empleado**: 1 hora 21 minutos  
> **Calificación**: 92.31 / 100  
> **Total preguntas**: 65

---

### Pregunta 1  
**Enunciado**:  
De acuerdo con el modelo de responsabilidad compartida de AWS, ¿cuál tarea es responsabilidad de AWS cuando se trata de cargas de trabajo que se ejecutan en Amazon EC2?

**Opciones**:  
- a. La actualización del hardware físico  
- b. La actualización de los datos de usuario  
- c. La actualización del sistema operativo  
- d. La actualización del motor de base de datos  

✅ **Respuesta correcta**: a. La actualización del hardware físico  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
El hardware físico forma parte de la responsabilidad de AWS.

---

### Pregunta 2  
**Enunciado**:  
De acuerdo con el modelo de responsabilidad compartida de AWS, ¿cuáles de las siguientes tareas son responsabilidad de AWS? (Seleccione DOS).

**Opciones**:  
- a. El parcheo de sistemas operativos en Amazon EC2.  
- b. El parcheo y la actualización del hipervisor.  
- c. La encriptación de los datos de los clientes.  
- d. La seguridad física de las instalaciones de AWS.  
- e. La definición de firewalls de red dentro del servicio VPC.  

✅ **Respuestas correctas**: b, d  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Al ser parte de la seguridad en la nube, aplicar parches y actualizar el hipervisor son responsabilidades de AWS. Es responsabilidad de AWS mantener la seguridad física de las instalaciones.

---

### Pregunta 3  
**Enunciado**:  
De acuerdo con el modelo de responsabilidad compartida de AWS, ¿qué tareas son responsabilidad del cliente? (Seleccione DOS).

**Opciones**:  
- a. Aplicar parches al sistema operativo invitado.  
- b. Configurar los firewalls.  
- c. Aplicar parches al hardware de la red.  
- d. Proteger físicamente el hardware del centro de datos.  
- e. Desactivar los dispositivos de almacenamiento obsoletos.  

✅ **Respuestas correctas**: a, b  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
El cliente tiene toda la responsabilidad de aplicar parches a los sistemas operativos y las aplicaciones. AWS no se hace responsable de aplicar parches al sistema operativo invitado. El cliente tiene la responsabilidad total de configurar todas las rutas de firewall en relación con el sistema operativo y la aplicación.

---

### Pregunta 4  
**Enunciado**:  
Desde múltiples recursos externos surgen ataques de inyección SQL dirigidos a una aplicación. ¿Cuál servicio o función de AWS puede ayudar a automatizar la mitigación en contra de estos ataques?

**Opciones**:  
- a. AWS WAF  
- b. Grupos de seguridad  
- c. ACL de red  
- d. Elastic Load Balancing (ELB)  

✅ **Respuesta correcta**: a. AWS WAF  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
AWS WAF es un firewall de aplicaciones web que ayuda a proteger sus aplicaciones web de las vulnerabilidades de seguridad más habituales que podrían afectar la disponibilidad de la aplicación, poner en riesgo la seguridad o consumir demasiados recursos.

---

### Pregunta 5  
**Enunciado**:  
Después de seleccionar una reserva de servidor dedicado de Amazon EC2, ¿qué opción de precios ofrecería el descuento más grande?

**Opciones**:  
- a. Pago por horas y bajo demanda  
- b. Pago total anticipado  
- c. Sin pago anticipado  
- d. Pago parcial anticipado  

✅ **Respuesta correcta**: b. Pago total anticipado  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
El pago total anticipado requiere de un pago completo previo. Esta opción de precios ofrece el descuento más grande.

---

### Pregunta 6  
**Enunciado**:  
Para un desarrollador web un ataque DDoS que tenga como objetivo una aplicación representa una preocupación. ¿Qué servicios o funciones de AWS pueden ayudar a proteger contra este tipo de ataques? (Seleccione DOS).

**Opciones**:  
- a. AWS Health Dashboard  
- b. AWS CloudTrail  
- c. Amazon CloudFront  
- d. AWS Shield  
- e. AWS Support  

✅ **Respuestas correctas**: c, d  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Shield Standard existe en CloudFront y Amazon Route 53, para ofrecer protección contra los ataques de DDoS. Shield es un servicio administrado de protección contra ataques de denegación de servicio distribuido (DDoS) que puede utilizar para ayudar a protegerse contra ellos.

---

### Pregunta 7  
**Enunciado**:  
Un desarrollador debe acceder a los recursos de AWS desde AWS CLI. ¿Qué función de AWS Identity and Access Management (IAM) puede utilizar el desarrollador para la autenticación?

**Opciones**:  
- a. Políticas de contraseña de la cuenta  
- b. Claves de acceso de IAM  
- c. Políticas de IAM  
- d. Las claves SSH  

✅ **Respuesta correcta**: b. Claves de acceso de IAM  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Las claves de acceso de IAM son credenciales a corto o largo plazo. Las claves de acceso le permiten acceder a AWS mediante programación.

---

### Pregunta 8  
**Enunciado**:  
Un profesional de la nube tiene la tarea de desarrollar un plan de recuperación ante desastres y pretende replicar datos entre múltiples áreas geográficas. ¿Cuál es el componente de la nube de AWS que la empresa debe utilizar para cumplir dichos requisitos?

**Opciones**:  
- a. Zonas de disponibilidad.  
- b. Regiones de AWS.  
- c. Cuentas de AWS.  
- d. Ubicaciones perimetrales.  

✅ **Respuesta correcta**: b. Regiones de AWS.  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Las regiones son el método adecuado para replicar datos en un plan de recuperación ante desastres.

---

### Pregunta 9  
**Enunciado**:  
Un sistema se recupera automáticamente de un error cuando una empresa inicia su carga de trabajo en la plataforma de servicios de la nube de AWS. ¿Qué pilar del marco de AWS Well-Architected demuestra esta situación?

**Opciones**:  
- a. Optimización de costos  
- b. Eficiencia de rendimiento  
- c. Fiabilidad  
- d. Excelencia operativa  

✅ **Respuesta correcta**: c. Fiabilidad  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
El pilar de fiabilidad se centra en las cargas de trabajo que realizan las funciones previstas y en cómo recuperarse rápidamente de un error para cumplir con las demandas. Uno de los principios de diseño del pilar de fiabilidad es la recuperación automática en caso de error.

---

### Pregunta 10  
**Enunciado**:  
Un usuario tiene petabytes de datos para migrar a AWS desde un área en la que no son posibles las conexiones de red de alta velocidad. ¿Cuál es el servicio MÁS RÁPIDO para transferir los datos?

**Opciones**:  
- a. AWS Batch  
- b. Amazon S3  
- c. AWS Snowball Edge  
- d. AWS VPN  

✅ **Respuesta correcta**: c. AWS Snowball Edge  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Snowball Edge ofrece un dispositivo robusto y seguro para la transferencia de datos. Con los dispositivos Snowball Edge puede migrar grandes cantidades de datos transportándolos físicamente sin usar Internet. Esta es una solución mucho más rentable y rápida que intentar enviar petabytes de información a través de Internet.

---

### Pregunta 11  
**Enunciado**:  
Una empresa aloja una aplicación en una instancia de Amazon EC2. La instancia de EC2 necesita acceder a varios recursos de AWS, incluidos Amazon S3 y Amazon DynamoDB. ¿Cuál es la solución MÁS eficiente para delegar permisos desde el punto de vista operativo?

**Opciones**:  
- a. Crear un usuario de IAM y utilizar su clave de acceso y clave de acceso secreta para crear un perfil CLI en la instancia de EC2.  
- b. Crear un rol de IAM con los permisos necesarios. Adjuntar el rol al usuario administrativo de IAM.  
- c. Crear un rol de IAM con los permisos necesarios. Adjuntar el rol a la instancia de EC2.  
- d. Crear un usuario de IAM y utilizar su clave de acceso y clave de acceso secreta en la aplicación.  

✅ **Respuesta correcta**: c. Crear un rol de IAM con los permisos necesarios. Adjuntar el rol a la instancia de EC2.  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Una solución que cree un rol de IAM con los permisos adecuados y lo adjunte a la instancia de EC2 proporcionará acceso a los recursos de AWS. Esta solución es una práctica recomendada de seguridad.

---

### Pregunta 12  
**Enunciado**:  
Una empresa cuenta con licencias de software que desea incorporar a AWS, pero el modelo de licencias exige licencias de núcleos físicos. ¿Cómo puede la empresa cumplir con este requisito en la nube de AWS?

**Opciones**:  
- a. Al crear una reserva de capacidad bajo demanda.  
- b. Al adquirir instancias reservadas dedicadas.  
- c. Al iniciar una instancia de Amazon EC2 con la tenencia predeterminada.  
- d. Al iniciar una instancia de Amazon EC2 en un servidor dedicado.  

✅ **Respuesta correcta**: d. Al iniciar una instancia de Amazon EC2 en un servidor dedicado.  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Un servidor dedicado puede aislar las instancias de EC2 de otras cuentas. Es posible controlar partes de la capa física. Los servidores dedicados permiten utilizar las licencias de software existentes.

---

### Pregunta 13  
**Enunciado**:  
Una empresa de venta al por menor en línea tiene picos de ventas de temporada varias veces al año, principalmente durante los días festivos. La demanda es menor en otros momentos. A la empresa le resulta difícil predecir el aumento de la demanda de infraestructura para cada temporada.  
¿Cuáles son las ventajas de migración a la nube de AWS que beneficiarían MÁS a la empresa? (Seleccione DOS).

**Opciones**:  
- a. Precios de pago por uso  
- b. Modelo de responsabilidad compartida de AWS  
- c. AWS Service Quotas  
- d. Elasticidad  
- e. Presencia global  

✅ **Respuestas correctas**: a, d  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
El modelo de precios de pago por uso le permite pagar únicamente por los recursos que utiliza. Con elasticidad, es posible beneficiarse al escalar hacia arriba y hacia abajo según sea necesario y dejar de adivinar las necesidades de capacidad de infraestructura.

---

### Pregunta 14  
**Enunciado**:  
Una empresa desea monitorear continuamente la actividad de las cuentas de AWS, incluidas las acciones que se llevan a cabo mediante la consola de administración de AWS, los kits de desarrollo de software (SDK) de AWS y las herramientas de línea de comandos. ¿Qué servicio de AWS cumple con estos requisitos?

**Opciones**:  
- a. Amazon CloudWatch  
- b. AWS CloudTrail  
- c. AWS Trusted Advisor  
- d. Amazon Inspector  

✅ **Respuesta correcta**: b. AWS CloudTrail  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
CloudTrail monitorea y registra continuamente la actividad en una cuenta de AWS. Los registros de CloudTrail incluyen las acciones que los usuarios realizan mediante la consola, los SDK, las llamadas API y AWS CLI.

---

### Pregunta 15  
**Enunciado**:  
Una empresa grande tiene una carga de trabajo que requiere que el hardware permanezca en las instalaciones. La empresa desea utilizar los mismos servicios de plano de administración y control que utiliza actualmente en AWS. ¿Qué servicio de AWS debería utilizar la empresa para cumplir con estos requisitos?

**Opciones**:  
- a. AWS Fargate  
- b. AWS Device Farm  
- c. AWS Ground Station  
- d. AWS Outposts  

✅ **Respuesta correcta**: d. AWS Outposts  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Outposts le permite utilizar el hardware instalado de AWS en las instalaciones para ampliar y ejecutar los servicios nativos de AWS disponibles en las instalaciones. Si usa Outposts, es posible ejecutar algunos servicios de AWS localmente mediante los mismos servicios, herramientas y las API de AWS.

---

### Pregunta 16  
**Enunciado**:  
Una empresa inicia una nueva aplicación en la nube de AWS. La aplicación se ejecutará en una instancia de Amazon EC2. Se necesitarán más instancias de EC2 cuando aumente la carga de trabajo. ¿Qué servicio o herramienta de AWS puede utilizar la empresa para iniciar la cantidad de instancias de EC2 necesarias para gestionar la carga de trabajo?

**Opciones**:  
- a. AWS Systems Manager  
- b. Amazon EC2 Auto Scaling  
- c. AWS App2Container (A2C)  
- d. Elastic Load Balancing (ELB)  

✅ **Respuesta correcta**: b. Amazon EC2 Auto Scaling  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Es posible utilizar Amazon EC2 Auto Scaling para hacer que más instancias de EC2 estén disponibles de forma automática con el fin de gestionar la carga de la aplicación.

---

### Pregunta 17  
**Enunciado**:  
Una empresa necesita acceso a ingenieros de soporte en la nube las 24 horas del día, los 7 días de la semana. ¿Cuál es el plan de AWS Support MENOS costoso que cumple este requisito?

**Opciones**:  
- a. AWS Basic Support  
- b. AWS Enterprise Support  
- c. AWS Business Support  
- d. AWS Developer Support  

✅ **Respuesta correcta**: c. AWS Business Support  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Business Support es el plan de soporte menos costoso que incluye acceso a ingenieros de soporte en la nube las 24 horas del día, los 7 días de la semana.

---

### Pregunta 18  
**Enunciado**:  
Una empresa necesita auditar sus recursos de AWS. La empresa debe documentar cualquier cambio que se hizo en los recursos.

**Opciones**:  
- a. Amazon Inspector  
- b. Amazon CloudWatch  
- c. AWS Config  
- d. AWS Artifact  

✅ **Respuesta correcta**: c. AWS Config  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
AWS Config es un servicio completamente administrado que puede proporcionar informes de auditoría del inventario y del historial de configuración de los recursos de AWS.

---

### Pregunta 19  
**Enunciado**:  
Una empresa necesita ejecutar una aplicación en instancias de Amazon EC2. La carga de trabajo en ejecución no se puede interrumpir. La empresa necesita una opción de compra de instancia que no requiera ningún compromiso. ¿Qué opción de compra de instancias cumplirá estos requisitos de la manera MÁS rentable?

**Opciones**:  
- a. Servidores dedicados  
- b. Instancias bajo demanda  
- c. Instancias reservadas  
- d. Instancias de spot  

✅ **Respuesta correcta**: b. Instancias bajo demanda  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Son ideales para cargas de trabajo críticas sin compromiso de tiempo.

---

### Pregunta 20  
**Enunciado**:  
Una empresa necesita transferir 60 TB de datos a la nube de AWS de forma segura. ¿Cuál de las siguientes opciones debe utilizar la empresa para cumplir con estos requisitos?

**Opciones**:  
- a. AWS Snowball Edge  
- b. Amazon Elastic Block Store (Amazon EBS)  
- c. Amazon S3  
- d. Amazon Elastic File System (Amazon EFS)  

✅ **Respuesta correcta**: a. AWS Snowball Edge  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Snowball Edge es un dispositivo de hardware con potencia de cómputo y almacenamiento incorporados. Snowball Edge transfiere datos entre su entorno local y la nube de AWS. Snowball Edge también puede realizar cargas de trabajo de procesamiento local y de cómputo perimetral. Snowball Edge admite terabytes de transferencia de datos.

---

### Pregunta 21  
**Enunciado**:  
Una empresa no posee un centro de datos físico, pero necesita una solución de red que conecte las computadoras portátiles de los empleados directamente a la nube de AWS. ¿Qué servicio de AWS cumplirá con este requisito?

**Opciones**:  
- a. AWS Outposts  
- b. Amazon CloudFront  
- c. AWS Client VPN  
- d. AWS Snowball Edge  

✅ **Respuesta correcta**: c. AWS Client VPN  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Client VPN es un servicio de VPN administrado basado en el cliente que le ofrece la posibilidad de acceder de forma segura a sus recursos de AWS y a los recursos de su red en las instalaciones.

---

### Pregunta 22  
**Enunciado**:  
Una empresa quiere alojar sus bases de datos relacionales en AWS. Las bases de datos tienen esquemas predefinidos que la empresa necesita replicar en AWS. ¿Qué servicios de AWS podría utilizar la empresa para las bases de datos? (Seleccione DOS).

**Opciones**:  
- a. Amazon Neptune  
- b. Amazon RDS  
- c. Amazon Aurora  
- d. Amazon DynamoDB  
- e. Amazon DocumentDB (compatible con MongoDB)  

✅ **Respuestas correctas**: b, c  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Amazon RDS es un servicio de base de datos administrado que admite motores de bases de datos relacionales. Aurora es un servicio de base de datos relacional completamente administrado y compatible con MySQL y PostgreSQL.

---

### Pregunta 23  
**Enunciado**:  
Una empresa quiere asegurarse de que dos instancias de Amazon EC2 estén en centros de datos independientes con una latencia de comunicación mínima entre los centros de datos. ¿Cómo puede la empresa cumplir con este requisito?

**Opciones**:  
- a. Al colocar una instancia de EC2 en las instalaciones y la otra en una región de AWS. A continuación, se conectan mediante una conexión de VPN de AWS.  
- b. Al colocar ambas instancias de EC2 en un grupo de ubicación para obtener un ancho de banda dedicado.  
- c. Al colocar las instancias de EC2 en dos regiones de AWS independientes conectadas mediante interconexión de VPC.  
- d. Al colocar las instancias de EC2 en dos zonas de disponibilidad independientes dentro de la misma región de AWS.  

✅ **Respuesta correcta**: d. Al colocar las instancias de EC2 en dos zonas de disponibilidad independientes dentro de la misma región de AWS.  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
El uso de dos zonas de disponibilidad en la misma región asegura una baja latencia y proporciona protección contra los errores de una zona de disponibilidad.

---

### Pregunta 24  
**Enunciado**:  
Una empresa quiere crear una aplicación de análisis de datos que utilice Amazon Redshift. La empresa necesita una estimación de costos para el uso futuro de Amazon Redshift. ¿Qué herramienta de AWS proporcionará una estimación de costos de alto nivel?

**Opciones**:  
- a. AWS Pricing Calculator.  
- b. Savings Plans.  
- c. AWS Budgets.  
- d. AWS Cost Explorer.  

✅ **Respuesta correcta**: a. AWS Pricing Calculator.  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
AWS Pricing Calculator permite crear estimaciones de costos para casos prácticos de AWS antes de implementarlos.

---

### Pregunta 25  
**Enunciado**:  
Una empresa quiere mejorar su postura de seguridad y auditoría limitando el acceso entrante a Amazon EC2.  
¿Qué debería usar la empresa para acceder a las instancias de forma remota en lugar de abrir los puertos SSH entrantes y administrar las claves SSH?

**Opciones**:  
- a. Pares de claves EC2  
- b. AWS Identity and Access Management (IAM)  
- c. Las ACL de red  
- d. AWS Systems Manager Session Manager  

✅ **Respuesta correcta**: d. AWS Systems Manager Session Manager  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Session Manager es un servicio de administración de nodos para la nube o para unidades de cómputo en las instalaciones. Session Manager proporciona una conexión segura mediante shell scripting. Es posible establecer la conexión sin necesidad de abrir puertos.

---

### Pregunta 26  
**Enunciado**:  
Una empresa quiere que sus empleados tengan acceso a la infraestructura de escritorios virtuales para acceder de forma segura a los escritorios que les proporcionan mediante los dispositivos personales de los empleados. ¿Qué servicio de AWS debería utilizar la empresa para cumplir con estos requisitos?

**Opciones**:  
- a. Amazon FSx para Windows File Server  
- b. Amazon AppStream 2.0  
- c. AWS AppSync  
- d. Amazon WorkSpaces  

✅ **Respuesta correcta**: d. Amazon WorkSpaces  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
WorkSpaces puede ejecutar un escritorio en la nube directamente en varios tipos de dispositivos. WorkSpaces se puede ejecutar en PC, Mac, iPad o Kindle Fire. Por lo tanto, los usuarios pueden interactuar de forma segura con los escritorios proporcionados por la empresa mediante sus dispositivos personales.

---

### Pregunta 27  
**Enunciado**:  
Una empresa tiene una aplicación sin estado que puede gestionar interrupciones. La aplicación debe estar disponible veinticuatro horas al día. El tráfico aumenta considerablemente durante el horario comercial. ¿Qué tipos de instancias para los picos de tráfico y de base tienen MÁS optimización de costos para cumplir con estos requisitos?

**Opciones**:  
- a. Instancias bajo demanda para tráfico base e instancias bajo demanda con escalado automático para picos de tráfico  
- b. Instancias reservadas tanto para el pico de tráfico como para el tráfico base  
- c. Instancias bajo demanda para el tráfico base e instancias de spot para los picos de tráfico mediante Amazon EC2 Fleet  
- d. Instancias reservadas para el tráfico base e instancias de spot para el pico de tráfico mediante Amazon EC2 Fleet  

✅ **Respuesta correcta**: d. Instancias reservadas para el tráfico base e instancias de spot para el pico de tráfico mediante Amazon EC2 Fleet  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Las instancias reservadas optimizan costos para el tráfico base. Las instancias de spot para picos de tráfico le permiten aprovechar los descuentos en la capacidad de EC2.

---

### Pregunta 28  
**Enunciado**:  
Una empresa tiene una aplicación web Java. La empresa desea utilizar la implementación automática para crear el entorno de AWS e implementar nuevas versiones de su aplicación.  
¿Qué servicio de AWS podría cumplir con estos requisitos?

**Opciones**:  
- a. Amazon EC2  
- b. AWS Control Tower  
- c. AWS Autoscaling  
- d. AWS Elastic Beanstalk  

✅ **Respuesta correcta**: d. AWS Elastic Beanstalk  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Elastic Beanstalk implementa y escala aplicaciones y servicios web. Elastic Beanstalk administra automáticamente la implementación, aprovisionamiento de capacidad, balanceo de carga, escalado automático y monitoreo.

---

### Pregunta 29  
**Enunciado**:  
Una empresa tiene una instancia de Amazon EC2 que debe acceder a AWS Secrets Manager para recuperar las credenciales.  
¿Qué identidad o servicio necesita la instancia de EC2 para realizar la tarea?

**Opciones**:  
- a. Autenticación multifactor (MFA)  
- b. Grupo de seguridad  
- c. Grupo de IAM  
- d. Rol de IAM  

✅ **Respuesta correcta**: d. Rol de IAM  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
La instancia de EC2 necesitará un perfil de instancias asociado a un rol de IAM para poder acceder a Secrets Manager. El rol de IAM proporcionará los permisos necesarios.

---

### Pregunta 30  
**Enunciado**:  
Una empresa traslada su oficina y debe establecer una conexión cifrada con AWS. ¿Qué servicio de AWS cumplirá con este requisito?

**Opciones**:  
- a. Amazon Connect  
- b. AWS VPN  
- c. AWS Direct Connect  
- d. Amazon Route 53  

✅ **Respuesta correcta**: b. AWS VPN  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
AWS proporciona AWS VPN como un servicio administrado. AWS VPN establece una conexión cifrada segura entre AWS y sus redes en las instalaciones o de sucursales.

---

### Pregunta 31  
**Enunciado**:  
¿Cuál es una responsabilidad de AWS en el modelo de responsabilidad compartida de AWS?

**Opciones**:  
- a. Configurar nuevos recursos dentro de una cuenta de AWS  
- b. Diseñar la aplicación de un cliente para la recuperación ante desastres  
- c. Actualizar los sistemas operativos invitados en las instancias de Amazon EC2 implementadas  
- d. Proteger la infraestructura física  

✅ **Respuesta correcta**: d. Proteger la infraestructura física  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
AWS mantiene totalmente los controles físicos.

---

### Pregunta 32  
**Enunciado**:  
¿Cuál de las siguientes opciones ayudará al usuario a determinar si necesita solicitar un aumento del límite de servicio de VPC?

**Opciones**:  
- a. AWS Trusted Advisor  
- b. AWS Health Dashboard  
- c. AWS Cost and Usage Report  
- d. AWS Service Catalog  

✅ **Respuesta correcta**: a. AWS Trusted Advisor  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Trusted Advisor realiza varias comprobaciones en su entorno de AWS y proporciona recomendaciones para mejorarlo. Una de las revisiones incluye las comprobaciones del límite del servicio de VPC.

---

### Pregunta 33  
**Enunciado**:  
¿Cuál de los siguientes es un beneficio que se obtiene al utilizar un servicio administrado de AWS?

**Opciones**:  
- a. Reducir la sobrecarga operativa para el personal de TI de una empresa.  
- b. Eliminar la necesidad de contar con una estrategia de respaldo.  
- c. Eliminar la necesidad de seguir los estándares de cumplimiento.  
- d. Incrementar los costos fijos que un equipo de finanzas puede predecir.  

✅ **Respuesta correcta**: a. Reducir la sobrecarga operativa para el personal de TI de una empresa.  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Los servicios administrados de AWS permiten ahorrar costos operativos con prácticas recomendadas.

---

### Pregunta 34  
**Enunciado**:  
¿Cuál es la responsabilidad compartida entre el usuario y los servicios de AWS?

**Opciones**:  
- a. Configurar una instancia de Amazon EC2  
- b. Proveer una clave para la encriptación del cliente de Amazon S3  
- c. Controlar el entorno de los centros de datos físicos de AWS  
- d. Proveer información y formación  

✅ **Respuesta correcta**: d. Proveer información y formación  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
AWS capacita al personal de AWS, pero un usuario debe capacitar a su propio personal. Por lo tanto, esta responsabilidad es un control compartido.

---

### Pregunta 35  
**Enunciado**:  
¿Cuál es un ejemplo de alta disponibilidad en la nube de AWS?

**Opciones**:  
- a. Implementación en cualquier parte del mundo con el uso de regiones de AWS  
- b. Disponibilidad de cualquier servicio de AWS para su uso mediante el pago bajo demanda  
- c. Asesoramiento del soporte técnico de AWS en cualquier momento del día  
- d. Garantía de la accesibilidad de una aplicación incluso si falla un recurso  

✅ **Respuesta correcta**: d. Garantía de la accesibilidad de una aplicación incluso si falla un recurso  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
La alta disponibilidad en la nube de AWS asegura que una aplicación permanezca accesible, incluso si falla un recurso. La arquitectura de alta disponibilidad está diseñada para no tener un solo punto de error.

---

### Pregunta 36  
**Enunciado**:  
¿Cuál es una práctica recomendada de AWS para administrar un usuario raíz de una cuenta de AWS?

**Opciones**:  
- a. Utilizar la autenticación multifactor (MFA) para el usuario raíz.  
- b. Crear una clave de acceso para el usuario raíz.  
- c. Compartir la contraseña del usuario raíz con el equipo de operaciones.  
- d. No rotar la contraseña del usuario raíz.  

✅ **Respuesta correcta**: a. Utilizar la autenticación multifactor (MFA) para el usuario raíz.  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Una práctica recomendada de AWS es activar la MFA para todos los usuarios, incluido el usuario raíz.

---

### Pregunta 37  
**Enunciado**:  
¿Cuál es una práctica recomendada de IAM para las claves de acceso del usuario raíz de la cuenta AWS?

**Opciones**:  
- a. Permitir que el grupo de administradores del sistema utilice las credenciales de usuario raíz para el acceso diario.  
- b. Utilizar las credenciales de usuario raíz para acceder a información confidencial almacenada en AWS  
- c. Utilizar las credenciales de usuario raíz para acceder a las instancias de bases de datos de producción.  
- d. De ser posible eliminar todas las claves de acceso del usuario raíz  

✅ **Respuesta correcta**: d. De ser posible eliminar todas las claves de acceso del usuario raíz  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
No se recomienda generar claves de acceso para el usuario raíz porque el usuario raíz provee acceso completo a los recursos de todos los servicios de AWS.

---

### Pregunta 38  
**Enunciado**:  
¿Cuáles de las siguientes son características de las regiones y zonas de disponibilidad de AWS? (Seleccione DOS).

**Opciones**:  
- a. Las regiones llevan los servicios de AWS a las instalaciones  
- b. Las regiones se encuentran a 100 km (60 millas) una de la otra  
- c. Las regiones constan de múltiples zonas de disponibilidad  
- d. Las regiones se encuentran en todo el mundo  
- e. Una zona de disponibilidad contiene varias regiones  

✅ **Respuestas correctas**: c, d  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Las regiones contienen múltiples áreas de implementación aisladas denominadas zonas de disponibilidad. Las regiones se encuentran en todo el mundo.

---

### Pregunta 39  
**Enunciado**:  
¿Cuáles de las siguientes son las prácticas recomendadas de seguridad para usar AWS Identity and Access Management (IAM)? (Seleccione DOS).

**Opciones**:  
- a. Rotar las credenciales con regularidad  
- b. Habilitar la autenticación multifactor (MFA)  
- c. No eliminar las credenciales incluso si nunca se utilizan  
- d. Utilizar políticas insertadas en lugar de políticas administradas por el cliente  
- e. Utilizar las credenciales de usuario raíz de la cuenta de AWS para las tareas de IAM  

✅ **Respuestas correctas**: a, b  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Una práctica recomendada de AWS es rotar las credenciales con regularidad. MFA proporciona una capa adicional de seguridad.

---

### Pregunta 40  
**Enunciado**:  
¿Cuáles de los siguientes son los principios de seguridad del marco de AWS Well-Architected? (Seleccione DOS).

**Opciones**:  
- a. Realizar operaciones como código  
- b. Proteger los datos en tránsito y en reposo  
- c. Monitorear, alertar y auditar las acciones y los cambios en los recursos de AWS  
- d. Analizar y atribuir los gastos  
- e. Implementar a nivel mundial en minutos  

✅ **Respuestas correctas**: b, c  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
La protección de los datos en tránsito y en reposo es un principio del pilar de seguridad. La trazabilidad incluye acciones de monitoreo y alerta.

---

### Pregunta 41  
**Enunciado**:  
¿Cuáles servicios o funciones de AWS pueden controlar el tráfico de VPC? (Seleccione DOS).

**Opciones**:  
- a. Grupos de seguridad  
- b. Amazon Connect  
- c. Las ACL de red  
- d. AWS Direct Connect  
- e. Amazon GuardDuty  

✅ **Respuestas correctas**: a, c  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Un grupo de seguridad funciona como un firewall virtual. Una ACL de red es una capa de seguridad adicional para VPC.

---

### Pregunta 42  
**Enunciado**:  
¿Cuáles son características de los usuarios y los grupos de AWS IAM? (Seleccione DOS).

**Opciones**:  
- a. Un usuario puede ser miembro de diferentes grupos.  
- b. Un usuario solo puede ser miembro de un grupo a la vez.  
- c. Los grupos solo pueden contener usuarios y no se pueden anidar.  
- d. Los grupos se pueden anidar y contener otros grupos.  
- e. Todos los usuarios nuevos se agregan automáticamente a un grupo predeterminado.  

✅ **Respuestas correctas**: a, c  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Es posible agregar un usuario a múltiples grupos. Un grupo de usuarios solo puede contener usuarios, pero no otros grupos.

---

### Pregunta 43  
**Enunciado**:  
¿Cuáles son los beneficios de migrar a la nube de AWS con respecto a mejorar el tiempo de comercialización?

**Opciones**:  
- a. Incrementar la agilidad empresarial  
- b. Disminuir la velocidad de implementación  
- c. Incrementar las capacidades de respaldo  
- d. Incrementar la seguridad de las aplicaciones  

✅ **Respuesta correcta**: a. Incrementar la agilidad empresarial  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Las empresas que se mudan a la nube de AWS pueden volverse más ágiles. Los recursos de TI están disponibles para su implementación en cuestión de minutos.

---

### Pregunta 44  
**Enunciado**:  
¿Qué beneficio de AWS permite a los usuarios implementar una infraestructura en la nube compuesta por múltiples regiones geográficas conectadas por una red de baja latencia, alto rendimiento y redundancia?

**Opciones**:  
- a. Seguridad  
- b. Economía de escala  
- c. Alcance global  
- d. Elasticidad  

✅ **Respuesta correcta**: c. Alcance global  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
La infraestructura global de AWS ofrece el beneficio de un alcance global. La infraestructura global de AWS consta de múltiples regiones geográficas que están conectadas por una red con baja latencia, alto rendimiento y redundancia.

---

### Pregunta 45  
**Enunciado**:  
¿Qué beneficios ofrece Amazon Rekognition?

**Opciones**:  
- a. La capacidad de detectar objetos que aparecen en las imágenes  
- b. La posibilidad de ofertar por trabajos de detección de objetos  
- c. La capacidad de cambiar el tamaño de millones de imágenes automáticamente  
- d. La posibilidad de colocar marcas de agua en las imágenes  

✅ **Respuesta correcta**: a. La capacidad de detectar objetos que aparecen en las imágenes  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Amazon Rekognition utiliza modelos de machine learning previamente entrenados para detectar objetos en las imágenes.

---

### Pregunta 46  
**Enunciado**:  
¿Qué función se puede utilizar para proteger los buckets de Amazon S3 contra sobreescrituras o eliminaciones accidentales?

**Opciones**:  
- a. Políticas de ciclo de vida  
- b. La encriptación del lado del servidor  
- c. Los puntos de acceso de S3  
- d. El control de versiones de un bucket  

✅ **Respuesta correcta**: d. El control de versiones de un bucket  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
El control de versiones de bucket permite mantener múltiples versiones de un objeto en un bucket de S3. Si elimina o sobrescribe accidentalmente un objeto, Amazon S3 no lo elimina permanentemente.

---

### Pregunta 47  
**Enunciado**:  
¿Qué opción es una función básica del AWS Cloud Adoption Framework (AWS CAF) desde el punto de vista de las operaciones?

**Opciones**:  
- a. Administrar el rendimiento y la capacidad.  
- b. Administrar los productos.  
- c. Administrar identidades y accesos.  
- d. Administrar la cartera de aplicaciones.  

✅ **Respuesta correcta**: a. Administrar el rendimiento y la capacidad.  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
La administración del rendimiento y la capacidad es una función de la perspectiva de las operaciones en AWS CAF.

---

### Pregunta 48  
**Enunciado**:  
¿Qué plan de AWS Support incluye un director técnico de cuenta (TAM) designado de AWS?

**Opciones**:  
- a. AWS Basic Support  
- b. AWS Developer Support  
- c. AWS Enterprise Support  
- d. AWS Business Support  

✅ **Respuesta correcta**: c. AWS Enterprise Support  
❌ **Tu respuesta**: d. AWS Business Support  

**Retroalimentación**:  
Business Support no incluye un TAM designado. Los TAM son solo una función del plan Enterprise On-Ramp Support y del plan Enterprise Support.

---

### Pregunta 49  
**Enunciado**:  
¿Qué principio de diseño de arquitectura se aplica al concepto de redimensionamiento de la infraestructura de la nube de AWS?

**Opciones**:  
- a. Realizar cambios frecuentes, pequeños y reversibles.  
- b. Optimizar los costos.  
- c. Escalar horizontalmente para aumentar la disponibilidad de la carga de trabajo.  
- d. Realizar operaciones como código.  

✅ **Respuesta correcta**: b. Optimizar los costos.  
❌ **Tu respuesta**: c. Escalar horizontalmente para aumentar la disponibilidad de la carga de trabajo.  

**Retroalimentación**:  
Es posible escalar horizontalmente para aumentar la disponibilidad de la carga de trabajo agregada como parte del pilar de fiabilidad. Sin embargo, esta solución no está relacionada con el redimensionamiento.

---

### Pregunta 50  
**Enunciado**:  
¿Qué principios de diseño de la nube de AWS pueden ayudar a aumentar la fiabilidad? (Seleccione DOS).

**Opciones**:  
- a. Medir la eficiencia general  
- b. Recuperación automática de errores  
- c. Utilizar arquitectura monolítica  
- d. Probar los procedimientos de recuperación  
- e. Adoptar un modelo de consumo  

✅ **Respuestas correctas**: b, d  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Este principio forma parte del pilar de fiabilidad del marco de AWS Well-Architected. En el evento en el que se detecte un error, se implementan procesos que pueden activarse sin intervención de manera manual.

---

### Pregunta 51  
**Enunciado**:  
¿Qué servicio de AWS ofrece el medio con MÁS optimización de costos para almacenar imágenes estáticas?

**Opciones**:  
- a. AWS Snowball Edge  
- b. Amazon Elastic Block Store (Amazon EBS)  
- c. Amazon S3  
- d. Amazon DynamoDB  

✅ **Respuesta correcta**: c. Amazon S3  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Amazon S3 es la opción con más optimización de costos para almacenar imágenes estáticas porque se paga por uso.

---

### Pregunta 52  
**Enunciado**:  
¿Qué servicio de AWS ofrece una forma sencilla de configurar un nuevo entorno de AWS con múltiples cuentas y gobernanza a escala?

**Opciones**:  
- a. AWS Trusted Advisor  
- b. AWS Security Hub  
- c. AWS Resource Access Manager  
- d. AWS Control Tower  

✅ **Respuesta correcta**: d. AWS Control Tower  
❌ **Tu respuesta**: b. AWS Security Hub  

**Retroalimentación**:  
Security Hub ofrece una visión exhaustiva de cómo su entorno de AWS se compara con las prácticas recomendadas de los estándares de seguridad. Security Hub no se usa para configurar y dirigir un entorno de cuentas múltiples.

---

### Pregunta 53  
**Enunciado**:  
¿Qué servicio de AWS puede alojar un sitio web estático?

**Opciones**:  
- a. Amazon Route 53  
- b. AWS X-Ray  
- c. Amazon QuickSight  
- d. Amazon S3  

✅ **Respuesta correcta**: d. Amazon S3  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Además de proporcionar un almacenamiento escalable de objetos con una alta disponibilidad, seguridad y rendimiento, Amazon S3 puede usarse para alojar un sitio web estático.

---

### Pregunta 54  
**Enunciado**:  
¿Qué servicio de AWS puede generar un hallazgo cuando la información de identificación personal (PII) se almacena en un bucket de Amazon S3?

**Opciones**:  
- a. Amazon Inspector  
- b. Amazon Macie  
- c. Amazon GuardDuty  
- d. AWS Trusted Advisor  

✅ **Respuesta correcta**: b. Amazon Macie  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Macie aplica técnicas de machine learning y coincidencia de patrones para identificar información confidencial, incluida la PII.

---

### Pregunta 55  
**Enunciado**:  
¿Qué servicio de AWS puede utilizar una empresa para detectar un corte en los servidores de su sitio web y para redirigir a los usuarios a servidores alternativos?

**Opciones**:  
- a. Amazon CloudFront  
- b. AWS Trusted Advisor  
- c. Amazon GuardDuty  
- d. Amazon Route 53  

✅ **Respuesta correcta**: d. Amazon Route 53  
❌ **Tu respuesta**: c. Amazon GuardDuty  

**Retroalimentación**:  
GuardDuty es un servicio de seguridad que monitorea sus cargas de trabajo para detectar actividad inusual y accesos sin autorización. En el evento de un corte, GuardDuty no redirige a los usuarios a servidores alternativos.

---

### Pregunta 56  
**Enunciado**:  
¿Qué servicio de AWS se debe utilizar para monitorear las instancias de Amazon EC2 para el uso de la CPU y la red?

**Opciones**:  
- a. Amazon Inspector  
- b. Amazon CloudWatch  
- c. AWS Config  
- d. AWS Cloudtrail  

✅ **Respuesta correcta**: b. Amazon CloudWatch  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
CloudWatch monitorea los recursos y recopila registros en tiempo real. A través de un agente de CloudWatch instalado en una instancia de EC2, se puede monitorear el uso de la CPU y la red.

---

### Pregunta 57  
**Enunciado**:  
¿Qué servicio de AWS se puede utilizar para migrar una base de datos en las instalaciones activa a la nube de AWS?

**Opciones**:  
- a. AWS Database Migration Service (AWS DMS)  
- b. AWS Storage Gateway  
- c. AWS DataSync  
- d. AWS Application Migration Service  

✅ **Respuesta correcta**: a. AWS Database Migration Service (AWS DMS)  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
AWS DMS migra las bases de datos relacionales, los almacenes de datos, las bases de datos NoSQL y otros almacenes de datos de las instalaciones a la nube de AWS.

---

### Pregunta 58  
**Enunciado**:  
¿Qué servicio de AWS utiliza machine learning para identificar la información confidencial que se almacena en los buckets de Amazon S3?

**Opciones**:  
- a. AWS Cloud9  
- b. Amazon Personalize  
- c. AWS CodeArtifact  
- d. Amazon Macie  

✅ **Respuesta correcta**: d. Amazon Macie  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Macie es un servicio de seguridad de datos que detecta información confidencial. Macie utiliza machine learning y coincidencia de patrones para identificar la información confidencial que se almacena en buckets de S3.

---

### Pregunta 59  
**Enunciado**:  
¿Qué servicio de base de datos de AWS proporciona almacenamiento de datos en memoria?

**Opciones**:  
- a. Amazon DynamoDB  
- b. Amazon ElastiCache  
- c. Amazon Timestream  
- d. Amazon RDS  

✅ **Respuesta correcta**: b. Amazon ElastiCache  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
ElastiCache es un servicio de almacenamiento en caché de datos en memoria completamente administrado para bases de datos.

---

### Pregunta 60  
**Enunciado**:  
¿Qué servicio de cómputo de AWS es serverless?

**Opciones**:  
- a. Amazon Elastic Container Service (Amazon ECS).  
- b. AWS Lambda.  
- c. Amazon EC2.  
- d. Amazon RDS.  

✅ **Respuesta correcta**: b. AWS Lambda.  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Lambda es un servicio sin servidor, administrado por AWS para parches, mantenimiento y capacidad.

---

### Pregunta 61  
**Enunciado**:  
¿Qué servicio o función de AWS puede usar un desarrollador para acceder a los servicios de AWS mediante programación?

**Opciones**:  
- a. Consola de administración de AWS  
- b. AWS CodeDeploy  
- c. Kits de desarrollo de software (SDK) de AWS  
- d. AWS CodePipeline  

✅ **Respuesta correcta**: c. Kits de desarrollo de software (SDK) de AWS  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Los usuarios pueden acceder mediante programación a los servicios de AWS a través de una API desde lenguajes de programación de su elección con AWS SDK.

---

### Pregunta 62  
**Enunciado**:  
¿Qué servicio o herramienta de AWS puede utilizar una empresa para visualizar, comprender y administrar el gasto y el uso de AWS conforme pasa el tiempo?

**Opciones**:  
- a. Amazon CloudWatch  
- b. AWS Cost Explorer  
- c. AWS Budgets  
- d. AWS Trusted Advisor  

✅ **Respuesta correcta**: b. AWS Cost Explorer  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Cost Explorer permite visualizar, comprender y administrar los gastos y el uso de AWS conforme pasa el tiempo.

---

### Pregunta 63  
**Enunciado**:  
¿Qué servicio puede utilizar un cliente para configurar una cuenta administrativa de pagador con el fin de ver los informes de facturación unificada?

**Opciones**:  
- a. AWS Organizations  
- b. Amazon QuickSight  
- c. AWS Budgets  
- d. Amazon Macie  

✅ **Respuesta correcta**: a. AWS Organizations  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Organizations es un servicio de administración de cuentas que le permite unificar múltiples cuentas de AWS para administrarlas de forma centralizada. La facturación unificada es una función de Organizations.

---

### Pregunta 64  
**Enunciado**:  
¿Qué tareas requieren el uso del usuario raíz de la cuenta de AWS? (Seleccione DOS).

**Opciones**:  
- a. Ejecutar aplicaciones en Amazon Elastic Kubernetes Service (Amazon EKS)  
- b. Restaurar los permisos de administrador de IAM  
- c. Modificar un tipo de instancia de Amazon EC2  
- d. Cerrar una cuenta de AWS  
- e. Agrupar recursos en AWS Systems Manager  

✅ **Respuestas correctas**: b, d  
🟢 **Tu respuesta**: Correcta  

**Retroalimentación**:  
Debe utilizar la cuenta de usuario raíz para restaurar los permisos de IAM si el único administrador de IAM revoca accidentalmente sus propios permisos. La cuenta raíz se debe usar para cerrar una cuenta de AWS.

---

### Pregunta 65  
**Enunciado**:  
Una aseguradora necesita archivar datos de clientes por HIPAA con acceso en 14 horas. ¿Qué clase de S3 es más apropiada?

**Opciones**:  
- a. Amazon S3 Glacier  
- b. Amazon S3 Standard  
- c. Amazon S3 Standard-IA  
- d. Amazon S3 Glacier Deep Archive  

✅ **Respuesta correcta**: d. Amazon S3 Glacier Deep Archive  
❌ **Tu respuesta**: a. Amazon S3 Glacier  

**Retroalimentación**:  
Deep Archive es más económico. Glacier Deep Archive ofrece recuperación en 12 horas (estándar), lo cual cumple con el requisito de <14 horas y es más barato que Glacier estándar.

---