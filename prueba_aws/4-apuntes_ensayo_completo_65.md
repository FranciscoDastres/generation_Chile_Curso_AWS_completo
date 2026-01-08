apuntes_ensayo_2
# Resumen de Servicios y Conceptos de AWS

## 1. Monitoreo y Auditoría
- **AWS CloudTrail**: Monitorea la actividad de cuentas de AWS registrando llamadas a la API.  
- **AWS Config**: Servicio de auditoría y monitoreo que documenta y rastrea cambios en los recursos de AWS, mantiene un historial de configuraciones y permite evaluar la conformidad de los recursos con políticas y reglas internas. También facilita la investigación de incidencias y la auditoría de seguridad.
- **Amazon CloudWatch**: Monitorea métricas de instancias EC2, uso de CPU, red y otros recursos.  
- **AWS Trusted Advisor**: Ayuda a verificar límites de servicio y recomendaciones de optimización, seguridad y costos.

## 2. Infraestructura y Computación
- **Instancias bajo demanda (EC2)**: Sin compromiso y sin interrupciones; cumplen con requisitos solicitados.  
- **EC2 Fleet**: Maximiza la confiabilidad y disponibilidad de instancias Spot.  
- **AWS Elastic Beanstalk**: Plataforma como Servicio (PaaS) que permite desplegar automáticamente aplicaciones web (por ejemplo, Java), creando y gestionando el entorno de AWS.  
- **Amazon ElastiCache**: Proporciona almacenamiento en memoria para aplicaciones con alta demanda de lectura.

## 3. Redes y Conectividad
- **AWS Client VPN**: Conecta empleados remotos de forma segura a recursos de AWS desde cualquier ubicación.  
- **AWS VPN**: Establece una conexión cifrada entre la oficina y AWS.  
- **AWS Direct Connect**: Conexión de red privada y dedicada entre un centro de datos on-premises y AWS.  
- **Amazon VPC**: Permite aislar recursos y configuraciones de red para distintos entornos.  
- **Alta disponibilidad en EC2**: Colocar instancias en distintas zonas de disponibilidad (AZ) dentro de la misma región para independencia y baja latencia.

## 4. Bases de Datos
- **Amazon RDS y Aurora**: Servicios administrados de bases de datos relacionales con esquemas definidos.  
- **AWS Database Migration Service (DMS)**: Migra bases de datos on-premises a la nube de AWS.  

## 5. Seguridad y Acceso
- **AWS IAM**: Gestión de usuarios, grupos y roles. Buenas prácticas:  
  - Rotar credenciales regularmente.  
  - Habilitar autenticación multifactor (MFA).  
  - Los grupos solo pueden contener usuarios, no se pueden anidar.  
- **AWS Systems Manager Session Manager**: Permite acceso remoto a instancias EC2 sin abrir puertos SSH ni gestionar claves, aumentando la seguridad.  
- **AWS WAF**: Firewall a nivel de aplicación para proteger apps web frente a vulnerabilidades y ataques maliciosos.  
- **Responsabilidad compartida de AWS**:  
  - AWS: proteger la infraestructura física.  
  - Cliente: proteger datos en tránsito, parchar aplicaciones en EC2 y gestionar la seguridad de los datos.  

## 6. Almacenamiento
- **Amazon S3**: Almacenamiento de objetos optimizado para imágenes estáticas.  
- **Control de versiones en S3**: Protege los buckets contra sobrescrituras o eliminaciones accidentales.  
- **Amazon S3 Glacier Deep Archive**: Almacenamiento de bajo costo para datos archivados, cumpliendo con requisitos como HIPAA con acceso en 14 horas.  

## 7. Servicios de Mensajería y Comunicación
- **Amazon SQS (Simple Queue Service)**: Cola de mensajes administrada que asegura que los mensajes entre componentes de software no se pierdan si falla uno o más componentes.

## 8. Machine Learning y Análisis
- **Amazon Rekognition**: Detecta objetos en imágenes.  
- **Amazon Macie**: Utiliza machine learning para identificar y proteger información sensible (PII) en buckets de S3.

## 9. Disponibilidad y Recuperación
- **Alta disponibilidad**: Garantiza accesibilidad de una app incluso si falla un recurso.  
- **Principios de fiabilidad AWS**: Recuperación automática de errores y pruebas de procedimientos de recuperación.  

## 10. Gobernanza y Gestión de Cuentas
- **AWS Control Tower**: Configura un entorno AWS con múltiples cuentas y gobernanza a escala.  
- **AWS Organizations**: Gestiona todas tus cuentas de AWS desde un solo lugar y permite crear cuentas administrativas de pagador para informes de facturación unificada.  

## 11. Optimización y Costos
- **Beneficios de servicios administrados**: Reducen la sobrecarga operativa del personal de TI.  
- **Optimización de costos**: Redimensionar infraestructura y automatizar donde sea posible.  
- **Planes de soporte AWS**:  
  - **Business Support**: Asistencia técnica 24/7 menos costosa.  
  - **Enterprise Support**: Incluye TAM (Technical Account Manager) designado.

## 12. Mejores Prácticas y Principios de Arquitectura
- **Usuario root**: Activar MFA y eliminar claves de usuario raíz.  
- **Principios de seguridad del Well-Architected Framework**: Proteger datos y monitorear.  
- **Principios de diseño importantes**: Automatizar donde sea posible y eliminar puntos únicos de falla.  
- **Beneficios de migrar a AWS**: Incremento de agilidad empresarial y reducción de gasto de capital.  
- **Alcance global**: Múltiples regiones geográficas conectadas por una red de baja latencia y alto rendimiento.

## 13. Otros
- **Opciones de compra de instancias EC2**: Dedicated Host permite BYOL (Bring Your Own License).  
- **Servicios de cómputo**: EC2 y Lambda.  
- **Pruebas de penetración en EC2**: El cliente puede realizarlas en sus propias instancias sin autorización previa de AWS.  
- **Automatización en AWS**: Buena práctica recomendada para reducir errores y mejorar eficiencia.  
- **Amazon Route 53**: Detecta fallas en servidores web y redirige a servidores alternativos.

