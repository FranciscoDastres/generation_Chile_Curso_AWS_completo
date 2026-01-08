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