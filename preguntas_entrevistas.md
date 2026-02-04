# Preguntas y respuestas para entrevista  
_Perfil: Ingeniero Informático | Cloud & Full Stack Developer (AWS + JavaScript)_

---

## AWS EC2

**P: ¿Qué es Amazon EC2 y para qué lo usarías en un proyecto?**  
R: Amazon EC2 es un servicio que permite lanzar máquinas virtuales en la nube para correr aplicaciones, servidores web, APIs o procesos de backend sin administrar hardware físico.[web:1]

**P: ¿Qué cosas sueles configurar al lanzar una instancia EC2?**  
R: Tipo de instancia (CPU/RAM), AMI o sistema operativo, par de claves para SSH, grupo de seguridad (puertos abiertos), VPC/subred y, opcionalmente, rol IAM asociado a la instancia.[web:1]

**P: ¿Cómo asegurarías una instancia EC2 expuesta a Internet?**  
R: Limitaría el tráfico en el Security Group solo a los puertos necesarios, restringiría SSH a IPs específicas, usaría roles IAM en vez de claves de acceso y mantendría el sistema actualizado con parches.[web:1]

---

## AWS S3

**P: ¿Para qué usarías Amazon S3 en una aplicación web?**  
R: Para almacenar archivos estáticos como imágenes, assets de frontend, backups o logs, aprovechando su alta durabilidad y disponibilidad y sirviéndolos mediante URLs directas o a través de CloudFront.[web:1]

**P: ¿Cómo controlarías quién puede leer o subir archivos a un bucket S3?**  
R: Mediante políticas de bucket y roles IAM, definiendo qué usuarios o servicios pueden listar, leer o escribir objetos, y evitando hacer el bucket completamente público salvo que sea estrictamente necesario.[web:1]

**P: ¿Qué es el versionado en S3 y cuándo es útil?**  
R: Es una característica que guarda múltiples versiones de un mismo objeto, útil para recuperar archivos borrados o sobrescritos por error y para auditoría de cambios.[web:1]

---

## AWS RDS

**P: ¿Qué es Amazon RDS y en qué se diferencia de una base de datos instalada en EC2?**  
R: RDS es un servicio administrado de bases de datos donde AWS se encarga de tareas como parches, backups automáticos y alta disponibilidad, mientras que en EC2 el usuario debe administrar el motor de base de datos por completo.[web:1]

**P: ¿Qué motores de base de datos de RDS te interesan como desarrollador Full Stack?**  
R: Principalmente PostgreSQL y MySQL, porque son motores relacionales muy usados en aplicaciones web y tienen buena integración con Node.js.[web:1]

**P: ¿Cómo protegerías una base de datos RDS en un entorno de producción?**  
R: Ubicándola en subredes privadas, controlando el acceso con grupos de seguridad para permitir solo conexiones desde las instancias de aplicación y usando credenciales seguras o autenticación IAM cuando esté disponible.[web:1]

---

## IAM (Identity and Access Management)

**P: ¿Qué problema resuelve IAM dentro de AWS?**  
R: IAM permite gestionar identidades y permisos, definiendo quién puede realizar qué acciones sobre qué recursos dentro de una cuenta de AWS.[web:1]

**P: ¿Qué es un rol IAM y cuándo lo usarías?**  
R: Un rol IAM es una identidad con permisos específicos que puede ser asumida por servicios o usuarios de forma temporal; por ejemplo, un rol que asume una instancia EC2 para leer objetos de un bucket S3 sin usar claves estáticas.[web:1]

**P: ¿Qué buenas prácticas sigues al trabajar con IAM?**  
R: Aplicar principio de mínimo privilegio, evitar incrustar Access Keys en el código, reutilizar políticas bien definidas y rotar credenciales en caso de usarlas.[web:1]

---

## VPC (nivel básico)

**P: ¿Qué es una VPC y por qué es importante?**  
R: Una VPC es una red virtual aislada dentro de AWS donde se definen rangos de IP, subredes, tablas de ruteo y reglas de seguridad, permitiendo diseñar la topología de red de forma controlada.[web:1]

**P: ¿Cómo separarías frontend y base de datos dentro de una VPC?**  
R: Colocaría las instancias que sirven HTTP en subredes públicas detrás de un load balancer y la base de datos (por ejemplo, RDS) en subredes privadas, accesibles solo desde el backend mediante grupos de seguridad.[web:1]

---

## CloudWatch

**P: ¿Para qué utilizarías Amazon CloudWatch en tus proyectos?**  
R: Para recolectar logs y métricas de servicios como EC2, RDS o aplicaciones propias, visualizar gráficos de rendimiento y configurar alarmas ante comportamientos anómalos.[web:1]

**P: Dame un ejemplo de una alarma útil en CloudWatch.**  
R: Una alarma que se active si la CPU de una instancia EC2 supera el 80% por más de 5 minutos, enviando una notificación al correo del equipo o a un canal de incidentes.[web:1]

---

## Backend con Node.js y Express

**P: ¿Cómo estructurarías una API REST con Node.js y Express?**  
R: Separando rutas, controladores y servicios; usando middlewares para autenticación, logging y manejo de errores; y conectando a la base de datos mediante un ORM o cliente SQL.[web:1]

**P: ¿Qué buenas prácticas sigues al diseñar endpoints REST?**  
R: Usar recursos y rutas claras, verbos HTTP correctos (GET, POST, PUT, DELETE), códigos de estado coherentes, validación de entrada y mensajes de error consistentes en formato JSON.[web:1]

**P: ¿Cómo manejarías los errores en una API hecha con Express?**  
R: Centralizando el manejo de errores en un middleware que capture las excepciones, loguee el detalle técnico y devuelva al cliente una respuesta con código adecuado y un mensaje controlado.[web:1]

---

## Frontend con JavaScript y React

**P: ¿Cómo organizas un proyecto React moderno?**  
R: Separando componentes por responsabilidad, usando hooks para manejar estado y efectos, creando servicios para llamadas a APIs y manteniendo una estructura clara de páginas, componentes y utilidades.[web:1]

**P: ¿Cómo consumirías tu propia API Node.js desde el frontend?**  
R: Creando un módulo de servicios que use `fetch` o una librería como Axios para llamar a la API, manejando errores y estados de carga, y usando ese módulo desde los componentes React.[web:1]

**P: ¿Qué significa que una interfaz sea responsiva y cómo lo implementas?**  
R: Que se adapta correctamente a distintos tamaños de pantalla; se implementa usando CSS responsive, frameworks como Tailwind o Bootstrap, y pruebas en diferentes dispositivos o tamaños de viewport.[web:1]

---

## Bases de datos: PostgreSQL y MySQL

**P: ¿Cuándo usarías una base de datos relacional como PostgreSQL o MySQL?**  
R: Cuando se necesita consistencia, relaciones claras entre entidades y soporte para consultas complejas con joins y transacciones.[web:1]

**P: ¿Cómo manejarías las migraciones de base de datos en un proyecto?**  
R: Usando herramientas de migración que permitan versionar cambios de esquema, aplicar y revertir migraciones y mantener sincronizados los entornos de desarrollo, staging y producción.[web:1]

---

## Preguntas típicas sobre tu experiencia (Codelium)

**P: Cuéntame de un logro técnico concreto en Codelium.**  
R: En Codelium optimicé el rendimiento de sistemas existentes, reduciendo los tiempos de carga en aproximadamente un 70% mediante mejoras en consultas, recursos estáticos y configuración del servidor.[file:2]

**P: ¿Cómo trabajabas en equipo y gestionaban las tareas?**  
R: Coordinábamos el trabajo usando SCRUM y Trello, definiendo sprints, priorizando tareas y manteniendo comunicación constante entre los desarrolladores para avanzar de forma ágil.[file:2]

**P: ¿Qué rol cumplías en la parte frontend y backend?**  
R: En frontend desarrollé interfaces responsivas con PHP y Tailwind CSS y componentes con JavaScript; en backend administré bases de datos MySQL y apoyé en el diseño de la lógica de negocio.[file:2]

---

## Cómo usar este documento

- Repasa las respuestas, pero exprésalas con tus propias palabras.  
- Prepara 2–3 ejemplos reales de proyectos donde hayas usado estos servicios.  
- Ten especialmente claros EC2, S3, IAM, RDS, CloudWatch y tu experiencia en Codelium, porque están directamente en tu CV.[file:2][file:1]
