# Panel de AWS Health (AWS Health Dashboard) - Guía de Estudio

## ¿Qué es AWS Health Dashboard?

AWS Health Dashboard es un servicio que proporciona visibilidad y notificaciones sobre el estado de servicios AWS que impactan tus recursos específicos. Te alerta sobre eventos que impactan tus servicios con contexto personalizado para tomar decisiones rápidas.

## Pitch / Propuesta de Valor

**¿Te enteras tarde de problemas que afectan tu cuenta?**

AWS Health te alerta sobre eventos que impactan tus servicios, con contexto personalizado para tomar decisiones rápidas.

## Función Principal

**Visualizar y recibir notificaciones sobre el estado de servicios AWS que impactan tus recursos**

AWS Health proporciona información relevante, oportuna y personalizada cuando eventos de AWS afectan tu infraestructura, permitiendo respuestas proactivas y planificadas.

## Características Clave

### Vista General y Personal de Salud

AWS Health ofrece dos dashboards complementarios:

#### Service Health Dashboard (Dashboard de Salud del Servicio)
- **Vista pública global** del estado de todos los servicios AWS
- Disponible para **todos** (incluso sin cuenta AWS)
- Muestra estado general por región
- Información histórica de incidentes
- Similar a otras páginas de status público

**URL**: https://health.aws.amazon.com/health/status

#### Personal Health Dashboard (Dashboard Personal de Salud) 
- **Vista personalizada** de eventos que **afectan TU cuenta específicamente**
- Requiere autenticación en cuenta AWS
- Filtra solo eventos relevantes a tus recursos
- Proporciona contexto sobre impacto en tu infraestructura
- **Mucho más valioso** que el dashboard público

### Historial de Eventos

#### Registro Completo
- Mantiene historial de todos los eventos que afectaron tu cuenta
- Eventos de servicio (interrupciones, degradaciones)
- Mantenimientos programados
- Cambios que afectan recursos
- Notificaciones de seguridad

#### Análisis y Auditoría
- Revisa eventos pasados para análisis post-mortem
- Correlaciona problemas de aplicación con eventos AWS
- Útil para reportes de disponibilidad
- Evidencia para SLAs y cumplimiento

### Impacto Detallado

AWS Health proporciona información específica sobre:

#### Recursos Afectados
- **Qué** recursos específicos están impactados (IDs de instancias, ARNs)
- **Cuándo** comenzó y cuándo se espera resolución
- **Dónde** (región/AZ específica)
- **Por qué** está ocurriendo el problema

#### Contexto del Impacto
- Severidad del evento (informacional, advertencia, crítico)
- Acciones recomendadas específicas
- Workarounds si están disponibles
- Timeline de resolución estimado

**Ejemplo:**
```
Evento: Degradación de rendimiento EC2
Recursos afectados: i-1234567890abcdef0, i-0987654321fedcba0
Región: us-east-1, AZ: us-east-1a
Impacto: Latencia incrementada en network
Acción recomendada: Migrar instancias a us-east-1b si es crítico
```

### Alertas Proactivas

#### Notificaciones Automáticas
- Alertas cuando eventos afectan tus recursos
- Notificaciones antes de mantenimientos programados
- Avisos de cambios deprecados en servicios que usas
- Alertas de seguridad relevantes

#### Canales de Notificación
- Email automático
- Integración con Amazon EventBridge
- Webhooks personalizados
- Integración con AWS Chatbot (Slack, Chime)

## Casos de Uso Típicos en el Examen

### 1. Seguimiento de Eventos que Afectan Cuentas Específicas
**Escenario**: Un equipo de operaciones necesita saber inmediatamente cuando ocurren problemas que afectan sus recursos de producción.

**Solución**: Configurar notificaciones de Personal Health Dashboard integrado con EventBridge para alertar automáticamente al equipo cuando eventos impactan recursos específicos.

### 2. Diagnósticos y Alertas Personalizadas
**Escenario**: Una aplicación experimenta problemas intermitentes. El equipo necesita determinar si es problema de su código o de AWS.

**Solución**: Revisar Personal Health Dashboard para correlacionar problemas de la app con eventos de servicio AWS (degradaciones, mantenimientos).

### 3. Mantenimientos Programados
**Escenario**: AWS necesita realizar mantenimiento en hardware que afecta instancias EC2. Necesitas planificar ventana de mantenimiento.

**Solución**: Personal Health Dashboard notifica con anticipación sobre mantenimientos programados, permitiendo planificar migraciones o ventanas de mantenimiento.

### 4. Cumplimiento y Auditoría
**Escenario**: Para auditoría, necesitas demostrar que interrupciones fueron causadas por problemas de AWS, no de tu aplicación.

**Solución**: Usar historial de eventos de Health Dashboard como evidencia documentada de interrupciones del proveedor.

## Integraciones Comunes

### CloudWatch
- Métricas y alarmas complementan eventos de Health
- CloudWatch muestra **qué** está pasando en tus recursos
- Health Dashboard muestra **por qué** (desde perspectiva AWS)
- Usa ambos para diagnóstico completo

### Amazon SNS (Simple Notification Service)
- Envía notificaciones de eventos de Health
- Distribuye alertas a múltiples suscriptores
- Integra con email, SMS, Lambda
- Escalamiento de notificaciones

### Amazon EventBridge
- **Integración principal** para automatización
- Dispara acciones automáticas basadas en eventos Health
- Filtra eventos específicos
- Orquesta respuestas multi-servicio

**Ejemplo de automatización:**
```
Evento Health: "Instancia EC2 programada para retiro"
   ↓
EventBridge Rule
   ↓
Lambda Function: Crear AMI → Lanzar nueva instancia → Actualizar ALB
   ↓
SNS: Notificar equipo de operaciones
```

### AWS Organizations con Personal Health Dashboard
- **Organizational View**: Vista agregada de eventos en todas las cuentas
- Requiere plan de soporte Business o Enterprise
- Dashboard centralizado para cuenta de management
- Visibilidad multi-cuenta desde un solo lugar

## Palabras Clave en Preguntas de Examen

Cuando veas estos términos, piensa en **AWS Health Dashboard**:

- **Estado del servicio**
- **Impacto en cuenta** / recursos específicos
- **Notificación** de eventos AWS
- **Evento operativo** / operational event
- Mantenimiento programado
- Personal Health Dashboard
- Alertas proactivas
- Recursos afectados
- Diagnóstico de problemas AWS
- Eventos específicos de cuenta

## Comparación: AWS Health vs Service Status Page vs CloudWatch

| Aspecto | AWS Health Dashboard | Service Status Page | CloudWatch |
|---------|---------------------|-------------------|------------|
| **Alcance** | Eventos AWS que afectan TU cuenta | Estado global de servicios AWS | Métricas de TUS recursos |
| **Personalización** | ✅ Específico a tus recursos | ❌ Información pública general | ✅ Tus recursos únicamente |
| **Requiere autenticación** | ✅ Sí (Personal Health) | ❌ No (público) | ✅ Sí |
| **Notificaciones** | ✅ Automáticas y personalizadas | ❌ No | ✅ Alarmas configurables |
| **Enfoque** | Eventos de AWS (externo) | Estado general AWS | Rendimiento de recursos (interno) |
| **Historial** | ✅ Eventos pasados | ⚠️ Limitado | ✅ Histórico de métricas |
| **Uso principal** | ¿Qué eventos AWS me afectan? | ¿Está AWS caído globalmente? | ¿Cómo están mis recursos? |

**Relación complementaria:**
- **CloudWatch**: "Mi CPU está al 100%" (síntoma)
- **Health Dashboard**: "AWS está haciendo mantenimiento en tu AZ" (causa)
- Úsalos juntos para diagnóstico completo

## Errores Comunes en el Examen

### ❌ Confundir Health Dashboard con Service Status Page global
- **Service Status Page**: Información pública, no personalizada, genérica
- **Personal Health Dashboard**: Específico a tu cuenta, personalizado, relevante
- El examen pregunta por notificaciones personalizadas → Personal Health Dashboard

### ❌ No aprovechar vistas personalizadas o alertas específicas
- Health Dashboard no es solo para "ver cuando AWS está caído"
- Proporciona alertas proactivas antes de que afecten tu servicio
- Úsalo para automatización y respuesta proactiva

### ❌ Pensar que es solo para interrupciones
- También notifica sobre: mantenimientos, deprecaciones, cambios de servicio
- Avisos de seguridad relevantes
- Actualizaciones que pueden afectar tu infraestructura

### ❌ No considerar Organizational View
- Para empresas con múltiples cuentas
- Vista centralizada desde cuenta de management
- Requiere Business o Enterprise Support

## Tipos de Eventos en AWS Health

### 1. Eventos de Servicio (Service Events)
**Afectan a múltiples clientes en una región/AZ**

#### Interrupciones (Outages)
- Servicios completamente no disponibles
- Impacto crítico en operaciones
- Severidad alta

#### Degradaciones (Degradations)
- Servicios funcionan pero con rendimiento reducido
- Latencia incrementada o throughput reducido
- Severidad media

#### Ejemplos:
- "Degradación de rendimiento en EC2 en us-east-1"
- "Interrupción de API de DynamoDB en ap-southeast-2"

### 2. Eventos de Cuenta (Account Events)
**Específicos a tu cuenta únicamente**

#### Mantenimientos Programados
- Hardware subyacente requiere mantenimiento
- Instancias EC2 programadas para retiro
- RDS maintenance windows

#### Cambios de Configuración
- Deprecaciones de APIs que usas
- Cambios en políticas que te afectan
- Actualizaciones de seguridad aplicables

#### Notificaciones de Facturación
- Cambios en precios de servicios que usas
- Finalización de free tier

#### Ejemplos:
- "Tu instancia i-1234 está programada para retiro el 2025-02-15"
- "RDS maintenance requerido para db-instance-prod-01"

### 3. Eventos de Seguridad
- Vulnerabilidades en servicios que usas
- Parches de seguridad requeridos
- Exposiciones de recursos detectadas

### 4. Eventos Informativos
- Nuevas características disponibles en tu región
- Mejores prácticas recomendadas
- Actualizaciones de documentación relevantes

## Organizational View

### ¿Qué es?

Vista **agregada** de eventos de AWS Health en **todas las cuentas** de tu AWS Organization.

### Requisitos
- Cuenta de AWS Organizations
- Plan de soporte **Business** o **Enterprise**
- Habilitar desde cuenta de management

### Beneficios

#### Visibilidad Centralizada
- Dashboard único para todas las cuentas
- No necesitas revisar cada cuenta individualmente
- Identifica patrones de eventos multi-cuenta

#### Gestión Proactiva
- Detecta problemas que afectan múltiples cuentas
- Prioriza respuesta basado en impacto organizacional
- Coordina resolución de problemas

#### Reportes Agregados
- Genera reportes de disponibilidad organizacionales
- Análisis de impacto en toda la organización
- Métricas de cumplimiento consolidadas

### Casos de Uso

**Escenario**: Empresa con 50 cuentas AWS necesita saber si un evento de servicio afecta recursos en múltiples cuentas.

**Solución**: Usar Organizational View para ver todos los eventos y recursos afectados en todas las cuentas desde un dashboard centralizado.

## Automatización con EventBridge

### Patrón de Automatización Común

#### 1. Crear Regla de EventBridge
```json
{
  "source": ["aws.health"],
  "detail-type": ["AWS Health Event"],
  "detail": {
    "eventTypeCategory": ["issue"],
    "service": ["EC2"]
  }
}
```

#### 2. Disparar Acciones Automáticas
- **Lambda**: Ejecutar remediación automática
- **SNS**: Notificar equipo de operaciones
- **Systems Manager**: Ejecutar runbooks de remediación
- **Step Functions**: Orquestar flujo de respuesta complejo

### Ejemplos de Automatización

#### Mantenimiento de EC2
```
Evento: "EC2 instance retirement scheduled"
   ↓
EventBridge → Lambda
   ↓
1. Crear snapshot de volumen
2. Crear AMI de la instancia
3. Lanzar nueva instancia en AZ diferente
4. Migrar Elastic IP
5. Notificar equipo via SNS
```

#### Degradación de DynamoDB
```
Evento: "DynamoDB performance degradation"
   ↓
EventBridge → Lambda
   ↓
1. Escalar read/write capacity automáticamente
2. Activar cache (DAX) si no está activo
3. Redirigir tráfico a réplica en otra región (si global table)
4. Alertar equipo
```

## Mejores Prácticas

1. **Configura notificaciones automáticas**: No dependas de revisar manualmente el dashboard
2. **Integra con EventBridge**: Automatiza respuestas a eventos comunes
3. **Usa Organizational View**: Si tienes múltiples cuentas, habilítalo
4. **Documenta eventos**: Mantén registro de eventos para análisis de tendencias
5. **Correlaciona con CloudWatch**: Usa ambos para diagnóstico completo
6. **Configura runbooks**: Ten procedimientos documentados para tipos de eventos comunes
7. **No ignores eventos informativos**: Pueden contener información sobre deprecaciones importantes
8. **Revisa historial periódicamente**: Identifica patrones de problemas recurrentes
9. **Integra con sistema de ticketing**: Crea tickets automáticos para eventos críticos
10. **Plan de soporte adecuado**: Business o Enterprise para Organizational View

## Planes de Soporte y Características

| Característica | Basic/Developer | Business | Enterprise |
|----------------|----------------|----------|------------|
| Personal Health Dashboard | ✅ | ✅ | ✅ |
| Notificaciones por email | ✅ | ✅ | ✅ |
| API de AWS Health | ❌ | ✅ | ✅ |
| EventBridge integration | ✅ | ✅ | ✅ |
| Organizational View | ❌ | ✅ | ✅ |
| Soporte proactivo | ❌ | ⚠️ Limitado | ✅ Completo |

## API de AWS Health

### Disponibilidad
- Requiere plan de soporte **Business** o **Enterprise**
- Acceso programático a eventos de Health
- Integración con herramientas personalizadas

### Casos de Uso
- Construir dashboards personalizados
- Integrar con sistemas ITSM (ServiceNow, Jira)
- Análisis y reportes automatizados
- Auditoría y cumplimiento

### Comandos AWS CLI

```bash
# Listar eventos actuales
aws health describe-events

# Obtener detalles de evento específico
aws health describe-event-details --event-arns arn:aws:health:us-east-1::event/EC2/...

# Listar recursos afectados por evento
aws health describe-affected-entities --filter eventArns=arn:aws:health:...

# Obtener tipos de eventos disponibles
aws health describe-event-types

# Ver eventos organizacionales (requiere Organizations)
aws health describe-events-for-organization
```

## Pricing (Precios)

### Personal Health Dashboard
- **GRATUITO** para todos los clientes AWS
- Sin cargos por consultar eventos
- Notificaciones por email incluidas

### Organizational View
- **Incluido** sin costo adicional en planes Business/Enterprise
- Pagas por el plan de soporte, no por Health específicamente

### API de AWS Health
- **Incluida** sin costo adicional en planes Business/Enterprise
- Sin cargos por llamadas a la API
- Pagas solo por servicios downstream (Lambda, SNS, etc.)

## Escenarios de Examen SAA-C03

### Escenario 1: Notificación de Mantenimiento
**Pregunta**: Una empresa necesita ser notificada con anticipación cuando AWS programa mantenimiento en sus instancias EC2 de producción para planificar ventanas de mantenimiento.

**Respuesta**: Configurar AWS Personal Health Dashboard con notificaciones automáticas. Integrar con EventBridge y SNS para alertar al equipo cuando se programan mantenimientos en instancias específicas.

### Escenario 2: Diagnóstico de Interrupciones
**Pregunta**: Durante un incidente, el equipo necesita determinar rápidamente si el problema es de su aplicación o de infraestructura AWS.

**Respuesta**: Revisar Personal Health Dashboard para correlacionar el timestamp del problema con eventos de servicio AWS. Combinar con métricas de CloudWatch para diagnóstico completo.

### Escenario 3: Automatización de Respuesta
**Pregunta**: Cuando AWS programa el retiro de una instancia EC2, el proceso de crear AMI y lanzar nueva instancia es manual y toma tiempo.

**Respuesta**: Crear regla de EventBridge que detecte eventos de "EC2 instance retirement" en Health Dashboard y dispare función Lambda que automatice: snapshot, AMI creation, nueva instancia, migración de Elastic IP.

### Escenario 4: Vista Multi-Cuenta
**Pregunta**: Una empresa con 100 cuentas AWS necesita visibilidad centralizada de eventos que afectan recursos en cualquier cuenta.

**Respuesta**: Habilitar Organizational View en Personal Health Dashboard (requiere Business/Enterprise support) para dashboard centralizado de eventos en todas las cuentas de la organización.

---

## Resumen Rápido para el Examen

**AWS Health Dashboard = Notificaciones Personalizadas de Eventos AWS**

- ✅ **Personal Health Dashboard**: Específico a TUS recursos (no genérico)
- ✅ **Notificaciones proactivas**: Antes de que problemas te afecten
- ✅ **Recursos afectados**: IDs específicos de instancias, ARNs
- ✅ **Historial de eventos**: Auditoría y análisis post-mortem
- ✅ **Integración EventBridge**: Automatización de respuestas
- ✅ **Organizational View**: Multi-cuenta (requiere Business/Enterprise)
- ❌ **NO es Service Status Page**: Ese es público y genérico
- ❌ **NO es CloudWatch**: CloudWatch monitorea TUS recursos, Health monitorea servicios AWS

**Palabras clave**: estado del servicio, impacto en cuenta, notificación, evento operativo, recursos afectados

**Complementario con:**
- CloudWatch (métricas de recursos) + Health (eventos AWS) = diagnóstico completo
- EventBridge para automatización de respuestas
- SNS para notificaciones distribuidas

**Cuándo usarlo**: Notificaciones de problemas AWS, mantenimientos programados, diagnóstico de interrupciones, auditoría de disponibilidad.
