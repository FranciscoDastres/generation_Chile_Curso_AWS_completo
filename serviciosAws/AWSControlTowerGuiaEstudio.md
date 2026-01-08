# AWS Control Tower - Guía de Estudio

## ¿Qué es AWS Control Tower?

AWS Control Tower es un servicio que automatiza la configuración de entornos multi-cuenta seguros y con buenas prácticas desde el inicio. Proporciona gobernanza centralizada y automatización para establecer y gestionar un entorno de AWS bien arquitectado.

## Pitch / Propuesta de Valor

**¿Tu nube crece sin control ni estándares?**

Control Tower establece cuentas seguras y gobernadas desde el inicio, con reglas predefinidas y automatización centralizada.

## Función Principal

**Automatizar la configuración de entornos multi-cuenta seguros y con buenas prácticas desde el inicio**

Control Tower simplifica la creación y gestión de múltiples cuentas de AWS aplicando automáticamente políticas de seguridad, cumplimiento y mejores prácticas organizacionales.

## Características Clave

### Landing Zone
Una landing zone es un entorno multi-cuenta preconfigurado que implementa:
- Estructura organizacional de cuentas
- Configuración de red base (VPCs, subnets)
- Políticas de seguridad y cumplimiento
- Logging y auditoría centralizada
- Acceso federado con AWS SSO

La landing zone es el **fundamento** sobre el cual construyes tu infraestructura AWS.

### Guardrails (Barreras de Seguridad)
Los guardrails son reglas de alto nivel que proporcionan gobernanza continua:

#### Guardrails Preventivos
- **Bloquean** acciones que violan políticas
- Implementados usando **Service Control Policies (SCPs)**
- No se pueden desactivar en cuentas gobernadas
- Ejemplos: Prevenir eliminación de logs, bloquear regiones no autorizadas

#### Guardrails Detectivos
- **Detectan** configuraciones no conformes
- Implementados usando **AWS Config Rules**
- Alertan sobre violaciones sin bloquear
- Ejemplos: Detectar buckets S3 públicos, instancias sin cifrado

### Account Factory
Servicio automatizado para crear nuevas cuentas de AWS con:
- Configuración estandarizada aplicada automáticamente
- Guardrails pre-configurados
- Estructura de OUs (Organizational Units) consistente
- Baseline de seguridad aplicado desde el primer momento
- Proceso self-service para equipos

**Ventaja clave**: Las nuevas cuentas se crean en minutos (vs días/semanas manualmente) con todas las políticas aplicadas.

### Consola Centralizada
Dashboard unificado que proporciona:
- Vista de todas las cuentas y su estado de cumplimiento
- Monitoreo de violaciones de guardrails
- Métricas de conformidad organizacional
- Gestión centralizada de políticas
- Visibilidad de drift (desviaciones de configuración)

## Casos de Uso Típicos en el Examen

### 1. Implementar Gobernanza Centralizada
**Escenario**: Una empresa necesita gestionar 50+ cuentas de AWS con políticas de seguridad consistentes.

**Solución**: Control Tower con guardrails para aplicar políticas automáticamente en todas las cuentas desde un punto central.

### 2. Habilitar Landing Zones
**Escenario**: Una organización está comenzando con AWS y necesita una estructura multi-cuenta bien arquitectada.

**Solución**: Implementar Control Tower para desplegar una landing zone con mejores prácticas de seguridad, red y logging.

### 3. Controlar Cuentas desde un Punto
**Escenario**: Diferentes equipos crean cuentas de AWS sin estándares, causando problemas de seguridad y cumplimiento.

**Solución**: Usar Account Factory de Control Tower para estandarizar la creación de cuentas con configuraciones y políticas pre-aprobadas.

### 4. Prevenir Drift (Desviación de Configuración)
**Escenario**: Los administradores modifican manualmente configuraciones críticas, violando políticas organizacionales.

**Solución**: Guardrails preventivos de Control Tower bloquean cambios no autorizados y detectivos alertan sobre desviaciones.

## Integraciones Comunes

### AWS Organizations
- **Base fundamental** de Control Tower
- Control Tower crea y gestiona la estructura de Organizations automáticamente
- Aplica SCPs a través de Organizations
- Gestiona OUs (Organizational Units)

### AWS Config
- Los guardrails detectivos usan Config Rules
- Monitoreo continuo de conformidad
- Historial de cambios de configuración
- Evaluación de cumplimiento multi-cuenta

### CloudTrail
- Logging centralizado de todas las actividades
- Auditoría de cambios en cuentas gobernadas
- Trazabilidad de acciones de usuarios
- Integración con Security Hub para análisis

### IAM / AWS SSO (Identity Center)
- Gestión centralizada de accesos
- Autenticación federada para usuarios
- Roles y permisos estandarizados
- Acceso basado en grupos y OUs

### Service Catalog
- Provisionamiento de recursos aprobados
- Plantillas estandarizadas para equipos
- Catálogo de productos conformes con políticas
- Self-service con controles de gobernanza

## Palabras Clave en Preguntas de Examen

Cuando veas estos términos, piensa en **AWS Control Tower**:

- **Multi-cuenta** / Multi-account
- **Gobernanza** centralizada
- **Landing zone**
- **Guardrail** (preventivo o detectivo)
- Automatización de cuentas
- Buenas prácticas desde el inicio
- Estructura organizacional
- Account Factory
- Cumplimiento multi-cuenta
- Configuración estandarizada

## Comparación: Control Tower vs Organizations vs Config

| Aspecto | Control Tower | Organizations | Config |
|---------|---------------|---------------|--------|
| **Propósito** | Automatización de gobernanza multi-cuenta | Agrupación y gestión básica de cuentas | Auditoría de configuración |
| **Nivel** | Solución completa (wrapper) | Servicio base | Servicio específico |
| **Complejidad** | Alto nivel, automatizado | Nivel medio, manual | Bajo nivel, específico |
| **Landing Zone** | ✅ Implementa automáticamente | ❌ No incluye | ❌ No incluye |
| **Guardrails** | ✅ Pre-configurados | ⚠️ Requiere configuración manual de SCPs | ⚠️ Requiere configuración manual de reglas |
| **Account Factory** | ✅ Incluido | ❌ No incluye | ❌ No aplica |
| **Uso ideal** | Nuevas implementaciones, estructuras grandes | Base para gestión de cuentas | Auditoría y cumplimiento específico |

**Relación**: Control Tower **usa** Organizations y Config internamente para proporcionar una solución completa y automatizada.

## Errores Comunes en el Examen

### ❌ Confundir Control Tower con Config o Organizations
- **Organizations**: Gestión básica de cuentas (sin automatización avanzada)
- **Config**: Auditoría de configuración (sin gobernanza multi-cuenta automática)
- **Control Tower**: Solución completa que usa ambos servicios para gobernanza automatizada

### ❌ No considerar su uso inicial en estructuras nuevas
- Control Tower es **ideal para implementaciones nuevas**
- Para cuentas existentes requiere migración y puede ser complejo
- Si ya tienes una estructura Organizations compleja, evalúa el esfuerzo de migración

### ❌ Ignorar la diferencia entre guardrails preventivos y detectivos
- **Preventivos**: Bloquean acciones antes de que ocurran (SCPs)
- **Detectivos**: Detectan problemas después de que ocurren (Config Rules)
- Algunos guardrails pueden estar en ambas categorías

## Arquitectura de Control Tower

### Estructura de Cuentas Base

#### Management Account (Cuenta de Gestión)
- Cuenta raíz de AWS Organizations
- Administra Control Tower
- **No se deben desplegar workloads aquí**

#### Log Archive Account (Cuenta de Archivo de Logs)
- Almacena todos los logs de CloudTrail
- Logs de AWS Config
- Acceso restringido solo para auditoría
- Retención a largo plazo

#### Audit Account (Cuenta de Auditoría)
- Acceso de solo lectura a todas las cuentas
- Para equipos de auditoría y cumplimiento
- Análisis de seguridad centralizado
- Integración con Security Hub y GuardDuty

#### Workload Accounts (Cuentas de Carga de Trabajo)
- Cuentas creadas con Account Factory
- Para desarrollo, testing, producción
- Organizadas en OUs (Organizational Units)
- Todos los guardrails aplicados automáticamente

### Organizational Units (OUs) Típicas

```
Root
├── Security OU
│   ├── Log Archive Account
│   └── Audit Account
├── Sandbox OU
│   └── Cuentas de experimentación (guardrails mínimos)
├── Development OU
│   └── Cuentas de desarrollo
├── Testing OU
│   └── Cuentas de testing
└── Production OU
    └── Cuentas de producción (guardrails estrictos)
```

## Tipos de Guardrails

### Por Nivel de Control

#### Mandatory (Obligatorios)
- **Siempre activos**, no se pueden deshabilitar
- Implementan mejores prácticas fundamentales de AWS
- Ejemplos:
  - Deshabilitar acceso público a buckets S3 de logs
  - Proteger logs de CloudTrail contra eliminación
  - Habilitar cifrado en volúmenes EBS

#### Strongly Recommended (Fuertemente Recomendados)
- Recomendados por AWS pero opcionales
- Implementan mejores prácticas de seguridad
- Ejemplos:
  - Habilitar MFA para acceso root
  - Detectar buckets S3 con versionado deshabilitado
  - Alertar sobre grupos de seguridad con acceso amplio

#### Elective (Electivos)
- Opcionales, según requisitos organizacionales
- Ejemplos:
  - Restringir regiones de AWS permitidas
  - Bloquear tipos de instancia EC2 específicos
  - Controlar uso de servicios específicos

### Por Comportamiento

#### Preventive (Preventivos)
- Usan **Service Control Policies (SCPs)**
- **Bloquean** acciones antes de que ocurran
- Retroalimentación inmediata (API devuelve error)

#### Detective (Detectivos)
- Usan **AWS Config Rules**
- **Detectan** problemas después de que ocurren
- Alertan sobre violaciones (no bloquean)

## Account Factory

### Características

- **Automatización completa** del aprovisionamiento de cuentas
- **Configuración baseline** aplicada automáticamente
- **Self-service** mediante Service Catalog
- **Estandarización** de todas las cuentas nuevas

### Proceso de Creación de Cuenta

1. Usuario solicita cuenta mediante Service Catalog
2. Account Factory valida la solicitud
3. Se crea la cuenta en la OU especificada
4. Se aplican guardrails según la OU
5. Se configuran redes baseline (VPC, subnets)
6. Se habilitan CloudTrail y Config
7. Se establecen permisos SSO
8. Cuenta lista para usar en minutos

### Configuraciones Aplicadas Automáticamente

- Estructura de red (VPCs, subnets, route tables)
- Habilitación de CloudTrail
- Configuración de AWS Config
- SCPs según OU
- Acceso SSO para grupos autorizados
- Tags de gestión y costos

## Drift Detection (Detección de Desviación)

Control Tower monitorea **drift** (desviaciones) de la configuración base:

### Tipos de Drift

- **Governance drift**: Cambios en guardrails o SCPs
- **Resource drift**: Modificaciones manuales en recursos gestionados
- **Moved resources**: Recursos movidos entre OUs

### Respuesta al Drift

- Dashboard muestra estado de drift
- Alertas automáticas sobre desviaciones
- **Repair**: Función para restaurar configuración correcta
- Re-registrar cuentas para re-aplicar configuración baseline

## Mejores Prácticas

1. **Comienza con Control Tower en nuevas implementaciones**: Más fácil que migrar
2. **Planifica tu estructura de OUs**: Diseña antes de implementar
3. **Usa Account Factory para todas las cuentas nuevas**: Garantiza consistencia
4. **Revisa el dashboard regularmente**: Identifica drift y violaciones
5. **No modifiques recursos gestionados manualmente**: Usa Control Tower para cambios
6. **Implementa guardrails progresivamente**: Comienza con mandatory, añade más gradualmente
7. **Integra con SSO/Identity Center**: Gestión centralizada de accesos
8. **Documenta excepciones**: Si deshabilitas guardrails, documenta el por qué
9. **Usa la cuenta de Management solo para gestión**: No despliegues aplicaciones
10. **Configura SNS para alertas**: Notificaciones proactivas de problemas

## Limitaciones

- Requiere una cuenta Organizations nueva o con estructura simple
- Migrar cuentas existentes puede ser complejo
- Algunos guardrails solo disponibles en regiones específicas
- No todos los servicios AWS están cubiertos por guardrails
- Costos adicionales por servicios subyacentes (Config, CloudTrail, etc.)

## Pricing (Precios)

AWS Control Tower **no tiene costo directo**, pero pagas por servicios subyacentes:

- **AWS Organizations**: Gratuito
- **AWS Config**: Por configuration items y evaluaciones de reglas
- **CloudTrail**: Por eventos registrados
- **Service Catalog**: Gratuito (pagas por recursos provisionados)
- **VPC**: Por recursos de red creados

**Estimación típica**: $50-200/mes por cuenta según uso de Config y volumen de logs.

## Comandos AWS CLI

```bash
# Listar landing zones
aws controltower list-landing-zones

# Obtener detalles de landing zone
aws controltower get-landing-zone --landing-zone-identifier <id>

# Listar guardrails habilitados
aws controltower list-enabled-controls

# Habilitar guardrail en OU
aws controltower enable-control --control-identifier <arn> --target-identifier <ou-arn>

# Deshabilitar guardrail
aws controltower disable-control --enabled-control-identifier <arn>

# Listar cuentas gestionadas
aws organizations list-accounts
```

## Escenarios de Examen SAA-C03

### Escenario 1: Nueva Estructura Multi-Cuenta
**Pregunta**: Una startup necesita configurar AWS desde cero con 20 cuentas para diferentes equipos y entornos, asegurando seguridad y cumplimiento.

**Respuesta**: Implementar AWS Control Tower para crear una landing zone con guardrails y usar Account Factory para provisionar cuentas estandarizadas automáticamente.

### Escenario 2: Gobernanza Centralizada
**Pregunta**: Una empresa tiene 100 cuentas AWS y necesita aplicar políticas de seguridad consistentes y prevenir que se eliminen logs de auditoría.

**Respuesta**: Migrar a Control Tower e implementar guardrails preventivos (SCPs) que bloqueen la eliminación de logs y detectivos (Config) que alerten sobre configuraciones no conformes.

### Escenario 3: Automatización de Aprovisionamiento
**Pregunta**: Los equipos solicitan nuevas cuentas AWS semanalmente. El proceso manual toma días y las cuentas tienen configuraciones inconsistentes.

**Respuesta**: Implementar Account Factory de Control Tower para que los equipos puedan auto-aprovisionar cuentas estandarizadas en minutos mediante Service Catalog.

### Escenario 4: Restricción de Regiones
**Pregunta**: Por cumplimiento regulatorio, una empresa debe prevenir que se creen recursos fuera de us-east-1 y eu-west-1.

**Respuesta**: Usar guardrails preventivos de Control Tower para denegar acceso a API de todas las regiones excepto las permitidas mediante SCPs.

---

## Resumen Rápido para el Examen

**AWS Control Tower = Gobernanza Automatizada Multi-Cuenta**

- ✅ **Landing Zone**: Entorno multi-cuenta preconfigurado
- ✅ **Guardrails**: Preventivos (bloquean) y Detectivos (alertan)
- ✅ **Account Factory**: Creación automatizada de cuentas estandarizadas
- ✅ **Consola Centralizada**: Vista unificada de cumplimiento
- ✅ **Usa Organizations + Config + CloudTrail** internamente
- ❌ **NO es solo Organizations** (es mucho más automatizado)
- ❌ **NO es solo Config** (es gobernanza completa)

**Palabras clave**: multi-cuenta, gobernanza, landing zone, guardrail, automatización, buenas prácticas

**Cuándo usarlo**: Nuevas implementaciones AWS, necesidad de gobernanza centralizada, múltiples cuentas con políticas consistentes.
