**AWS CloudTrail** es un servicio de auditoría y monitoreo que registra todas las llamadas a la API dentro de una cuenta de AWS, incluyendo acciones realizadas a través de la 
**consola de AWS**, **SDKs**, **CLI** y otros servicios de AWS.

## Características principales

- **Registro de eventos**
  - Captura **eventos de gestión**: cambios de configuración, creación/eliminación de recursos.
  - Captura **eventos de datos**: operaciones sobre recursos específicos como S3 y Lambda.
  - Cada evento incluye: usuario, hora, acción, recursos afectados y origen de la solicitud.

- **Almacenamiento seguro y duradero**
  - Los logs se pueden enviar automáticamente a **Amazon S3**.
  - Se pueden **cifrar con AWS KMS** para mayor seguridad.

- **Monitoreo en tiempo real**
  - Integración con **Amazon CloudWatch Logs** para generar alertas ante eventos críticos.

- **Análisis y auditoría**
  - Permite **buscar y filtrar eventos** específicos.
  - Facilita auditorías de seguridad y cumplimiento regulatorio.

- **Multi-región y multi-cuenta**
  - Posibilidad de registrar eventos de **todas las regiones** y **cuentas** dentro de una organización de AWS.

- **Integración con otros servicios**
  - Compatible con **AWS Config** para evaluación de conformidad.
  - Puede integrarse con **Amazon Athena** para consultas avanzadas de logs.

- **Retención y gestión de logs**
  - Configuración de **políticas de retención en S3**.
  - Permite **archivar logs automáticamente** según necesidades de cumplimiento.  

  * que es ? 
  # es un servcicio de auditoria que registra todas las llamadas de la API dentro de una cuenta de AWS, incluyendo acciones realizadas a traves de
   * consola aws
   * SDKs
   * CLI
  # responde a quien hizo que y cuando desde donde

  * sirve para
   # Auditoria
   # Seguridad
   # Cumplimiento normativo
   # Investigacion de incidentes
    * saber quien borro un recurso
    * detectar accesos no autorizados
    * cumplir normas (ISO 27001 , PCI DSS, SOC control de accesos y cambios, GDPR / Ley de datos / quien accede a los datos)
  * como funciona
  # cloud trail registra eventos
   * acciones de consola
   * llamadas API
   * CLI / SDK
  # Guarda logs en
   * S3
   * CloudWatch Logs
  
  * Es historico no solo en tiempo real
 
  * Cuando usarlo 
  # Necesitas auditoria
  # Quieres trazabilidad
  # Investigas incidentes
  # Requieres compliance (hacer que  cumpla las rejas )

 * Pregunta tipo examen
 # Empresa necesita saber quien modifico una política IAM

 * Cloudtrail existe para dejar evidencia de TODO lo que pasa en AWS

 * Correcto. CloudTrail monitorea y registra continuamente la actividad en una cuenta de AWS. Los registros de CloudTrail incluyen las acciones que los usuarios realizan mediante la consola, los SDK, las llamadas API y AWS CLI.

*  CloudTrail ayuda con la gobernanza, el cumplimiento y la auditoría operativa y de riesgos de las cuentas de AWS. CloudTrail no protege contra los ataques de DDoS.
