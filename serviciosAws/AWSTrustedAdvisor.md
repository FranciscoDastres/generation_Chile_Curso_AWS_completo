# AWS Trusted Advisor - Guía Completa

## ¿Qué es AWS Trusted Advisor?

AWS Trusted Advisor es un servicio automatizado de AWS que inspecciona tu entorno de nube y proporciona recomendaciones en tiempo real basadas en las mejores prácticas de Amazon Web Services. Actúa como un consultor virtual que analiza continuamente tu infraestructura para ayudarte a optimizar costos, mejorar el rendimiento, aumentar la seguridad y la resiliencia.

## Los 5 Pilares de Trusted Advisor

### 1. Optimización de Costos
- Identifica recursos no utilizados o subutilizados
- Recomienda instancias reservadas para ahorrar costos
- Detecta volúmenes de EBS sin asociar
- Analiza oportunidades de ahorro en servicios como RDS, EC2, y Lambda
- Sugiere eliminación de recursos inactivos

### 2. Rendimiento
- Evalúa la configuración de servicios para maximizar velocidad
- Analiza el uso de throughput en volúmenes de EBS
- Revisa límites de servicio que podrían afectar el rendimiento
- Examina la distribución de contenido con CloudFront
- Optimiza configuraciones de bases de datos RDS

### 3. Seguridad
- Verifica grupos de seguridad con puertos abiertos al público
- Detecta buckets de S3 con permisos públicos
- Revisa el uso de MFA (autenticación multifactor)
- Analiza certificados SSL/TLS expirados
- Comprueba el uso de credenciales de acceso antiguas
- Evalúa políticas de IAM demasiado permisivas

### 4. Tolerancia a Fallos (Resiliencia)
- Verifica configuraciones de alta disponibilidad
- Analiza redundancia en diferentes zonas de disponibilidad
- Revisa backups y snapshots de EBS
- Examina configuraciones de Auto Scaling
- Evalúa la configuración de Route 53 para failover

### 5. Límites de Servicio
- Monitorea el uso actual vs límites de servicios
- Notifica cuando te acercas a los límites (80% o más)
- Permite solicitar incrementos de límites proactivamente
- Previene interrupciones por alcanzar cuotas máximas

## Sistema de Códigos de Color

Trusted Advisor utiliza un sistema visual para priorizar acciones:

- 🟢 **Verde**: Sin problemas detectados
- 🟡 **Amarillo**: Investigación recomendada (no crítico)
- 🔴 **Rojo**: Acción recomendada (requiere atención)
- 🔵 **Azul**: Más del 80% del límite de servicio alcanzado

## Niveles de Acceso Según Plan de Soporte

### Plan Basic y Developer (Gratuito)
- Acceso limitado a 7 comprobaciones básicas de seguridad y rendimiento
- Comprobaciones de límites de servicio
- Sin notificaciones automáticas
- Sin acceso a API

### Plan Business y Enterprise
- Acceso completo a todas las comprobaciones (más de 115 checks)
- Notificaciones semanales por correo electrónico
- Acceso a la API de Trusted Advisor
- **Trusted Advisor Priority**: Recomendaciones priorizadas por tu equipo de cuentas
- Vista organizacional para múltiples cuentas
- Integración con Amazon EventBridge
- Capacidad de exclusión de recursos

## Funcionalidades Avanzadas

### Vista Organizacional
- Crea informes agregados para todas las cuentas de AWS Organizations
- Descarga informes en formato JSON o CSV
- Visualiza el estado de todas las cuentas en un solo dashboard
- Identifica patrones y problemas comunes en la organización

### Trusted Advisor Priority
- Recomendaciones contextualizadas según tus prioridades empresariales
- Personalización por tu equipo de cuentas técnicas (TAM)
- Enfoque en los checks más relevantes para tu negocio
- Reduce el ruido de alertas innecesarias

### Integraciones

#### Amazon EventBridge
- Automatiza respuestas a cambios en el estado de checks
- Crea flujos de trabajo personalizados
- Integra con Lambda para remedición automática
- Envía notificaciones a sistemas externos

#### AWS Support API
- Acceso programático a resultados de Trusted Advisor
- Integración con herramientas de monitoreo personalizadas
- Automatización de reportes
- Construcción de dashboards personalizados

#### AWS Systems Manager
- Ejecuta acciones correctivas automáticas
- Integra con runbooks para remedición
- Automatiza respuestas a problemas detectados

## Comprobaciones Destacadas

### Seguridad
- Grupos de seguridad - Puertos sin restricciones
- Buckets de S3 con permisos de lectura/escritura públicos
- IAM - Uso de credenciales de usuario root
- MFA en cuenta root
- Rotación de claves de acceso IAM

### Costos
- Instancias EC2 de baja utilización
- Direcciones IP elásticas no asociadas
- Instancias RDS inactivas
- Volúmenes EBS sin asociar
- Recomendaciones de instancias reservadas

### Rendimiento
- Instancias EC2 sobreutilizadas
- Throughput de volúmenes EBS
- Balanceadores de carga sin instancias saludables
- Configuración de CloudFront

## Mejores Prácticas

1. **Revisión Regular**: Accede al dashboard al menos semanalmente
2. **Actúa en Rojos Primero**: Prioriza las alertas rojas que requieren acción inmediata
3. **Automatiza Respuestas**: Usa EventBridge y Lambda para remediar problemas comunes
4. **Configura Notificaciones**: Habilita alertas por correo para cambios críticos
5. **Usa Exclusiones Inteligentemente**: Excluye solo recursos con justificación válida
6. **Documenta Decisiones**: Mantén registro de por qué ciertos checks se ignoran
7. **Vista Organizacional**: Si tienes múltiples cuentas, usa la vista consolidada
8. **Integra con ITSM**: Conecta con ServiceNow, Jira u otras herramientas de tickets

## Limitaciones

- No todos los checks están disponibles en todas las regiones
- Algunas recomendaciones pueden no aplicar a arquitecturas específicas
- Los checks se ejecutan periódicamente (no en tiempo real continuo)
- Requiere permisos IAM adecuados para funcionar correctamente
- Plan gratuito tiene acceso muy limitado

## Acceso y Permisos IAM

### Permisos Requeridos
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "trustedadvisor:Describe*",
      "trustedadvisor:RefreshCheck",
      "support:DescribeTrustedAdvisorChecks",
      "support:DescribeTrustedAdvisorCheckResult",
      "support:RefreshTrustedAdvisorCheck"
    ],
    "Resource": "*"
  }]
}
```

## Costo

- **Plan Basic/Developer**: Acceso limitado sin costo adicional
- **Plan Business**: Desde $100/mes o 10% de uso de AWS mensual (lo que sea mayor)
- **Plan Enterprise**: Desde $15,000/mes
- No hay cargo adicional por usar Trusted Advisor más allá del plan de soporte

## Recursos Adicionales

- Consola web: AWS Console > Support > Trusted Advisor
- API Documentation: AWS Support API
- Integraciones: EventBridge, CloudWatch, Systems Manager
- Reportes: JSON, CSV descargables

---

**Nota**: Trusted Advisor es una herramienta fundamental para mantener un entorno AWS optimizado, seguro y eficiente. Para aprovechar al máximo sus capacidades, considera actualizar a un plan de soporte Business o Enterprise si tu organización depende críticamente de AWS.

* Que es 
# servicio que analiza tu cuenta de AWS y te da recomendaciones basadas en best practices de AWS
# no ejecuta cambios recomienda!

* Para que sirve
# mejorar costos,seguridad,rendimiento,limites de servicio,tolerancia a fallos
# un asesor automatico de AWS

* Como funciona
# analiza recursos de tu cuenta
# compara best practices
# genera checks
# muestra recomendaciones
# te dice que mejorar y porque
# tu decides si aplicas los cambios

* Cuando usarlo
# quiereres optimizar costos
# Buscas mejorar la seguridad
# Quieres cunplir buenas practicas
# Necesitas revisar limites

* Ejemplo de examen
# empresa quiere recomendaciones automaticas para reducir costos y mejorar seguridad