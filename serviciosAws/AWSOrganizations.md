# AWS Organizations - Guía de Estudio

## ¿Qué es AWS Organizations?

AWS Organizations es un servicio de gestión de cuentas que permite administrar múltiples cuentas AWS desde una jerarquía central con políticas unificadas. Centraliza el control, aplica políticas unificadas y simplifica la facturación entre cuentas.

## Pitch / Propuesta de Valor

**¿Administrar múltiples cuentas AWS es una pesadilla?**

Organizations centraliza el control, aplica políticas unificadas y simplifica la facturación entre cuentas.

## Función Principal

**Gestionar múltiples cuentas AWS desde una jerarquía central con políticas unificadas**

Organizations proporciona un framework para consolidar múltiples cuentas bajo una organización única, permitiendo gestión centralizada de seguridad, cumplimiento, y facturación.

## Características Clave

### Organizational Units (OUs) - Unidades Organizacionales

Las OUs son contenedores jerárquicos para agrupar cuentas AWS:

#### Estructura y Propósito
- Agrupan cuentas por función, departamento o entorno
- Permiten aplicar políticas a múltiples cuentas simultáneamente
- Pueden anidarse hasta 5 niveles de profundidad
- Facilitan la delegación de administración

#### Ejemplos de Estructura

```
Root
├── Production OU
│   ├── Frontend-Prod Account
│   ├── Backend-Prod Account
│   └── Database-Prod Account
├── Development OU
│   ├── Dev-Team-A Account
│   └── Dev-Team-B Account
├── Security OU
│   ├── Security-Tools Account
│   └── Audit-Logging Account
└── Sandbox OU
    └── Experimental Accounts
```

#### Beneficios de OUs
- Aplicación de políticas en cascada
- Segregación lógica de recursos
- Facilitación de cumplimiento regulatorio
- Estructura organizacional clara

### Service Control Policies (SCPs)

SCPs son políticas JSON que definen los **permisos máximos** disponibles en cuentas y OUs:

#### Características de SCPs
- **No otorgan permisos**: Solo establecen límites máximos
- Funcionan como "filtros" sobre permisos IAM
- Se aplican a nivel de cuenta o OU
- Se heredan en cascada desde el root
- Afectan a todos los usuarios y roles (incluso root de cuenta)

#### Importante: SCPs ≠ IAM
```
Permisos efectivos = Permisos IAM ∩ SCPs aplicables

Si SCP niega algo → Bloqueado (incluso si IAM permite)
Si SCP permite algo → Aún requiere permisos IAM
```

#### Estrategias de SCPs

**Allow List (Lista de Permitidos)**
- Por defecto niega todo
- Explícitamente permite servicios/acciones específicas
- Más seguro pero requiere más mantenimiento
- Ideal para entornos altamente regulados

**Deny List (Lista de Denegados)**
- Por defecto permite todo (FullAWSAccess)
- Explícitamente niega servicios/acciones específicas
- Más flexible pero menos restrictivo
- Más común en implementaciones

#### Ejemplos de Uso

**Restringir regiones permitidas:**
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Deny",
    "Action": "*",
    "Resource": "*",
    "Condition": {
      "StringNotEquals": {
        "aws:RequestedRegion": ["us-east-1", "us-west-2"]
      }
    }
  }]
}
```

**Prevenir desactivación de CloudTrail:**
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Deny",
    "Action": [
      "cloudtrail:StopLogging",
      "cloudtrail:DeleteTrail"
    ],
    "Resource": "*"
  }]
}
```

### Control Centralizado

Organizations proporciona gestión centralizada de:

#### Políticas
- Service Control Policies (SCPs)
- Tag Policies (políticas de etiquetado)
- Backup Policies (políticas de respaldo)
- AI Services Opt-out Policies

#### Seguridad
- Gestión de acceso entre cuentas
- Compartir recursos con AWS RAM
- Auditoría centralizada con CloudTrail
- Análisis de seguridad con Security Hub

#### Facturación
- Consolidated Billing (Facturación consolidada)
- Descuentos por volumen agregado
- Reservas compartidas entre cuentas
- Savings Plans organizacionales

### Integración con Control Tower y Budgets

#### Con Control Tower
- Organizations es la **base fundamental** de Control Tower
- Control Tower crea y gestiona la estructura de Organizations automáticamente
- SCPs implementan los guardrails preventivos de Control Tower
- Control Tower añade automatización sobre Organizations

**Diferencia clave:**
- **Organizations**: Gestión manual, requieres configurar todo
- **Control Tower**: Automatización completa sobre Organizations

#### Con AWS Budgets
- Crea presupuestos para toda la organización
- Monitorea gastos agregados por OU
- Alertas centralizadas de sobrecostos
- Integra con facturación consolidada

## Casos de Uso Típicos en el Examen

### 1. Gobernanza Multi-Cuenta
**Escenario**: Empresa con 50 cuentas AWS necesita aplicar políticas de seguridad consistentes sin configurar cada cuenta individualmente.

**Solución**: Usar Organizations con OUs para agrupar cuentas y SCPs para aplicar políticas centralizadamente.

### 2. Consolidación de Facturación
**Escenario**: Departamentos pagan individualmente por AWS y no obtienen descuentos por volumen.

**Solución**: Consolidar cuentas en Organizations para facturación única y descuentos agregados.

### 3. Políticas de Acceso por Unidad Organizacional
**Escenario**: El equipo de desarrollo no debe acceder a servicios de producción ni regiones específicas.

**Solución**: Crear Development OU con SCPs que denieguen acceso a regiones de producción y servicios críticos.

## Integraciones Comunes

### IAM (Identity and Access Management)
- SCPs trabajan junto con políticas IAM
- SCPs establecen límites máximos, IAM otorga permisos
- Ambos son necesarios para acceso efectivo
- SCPs afectan a toda la cuenta incluyendo root

### AWS Config
- Monitorea cumplimiento de configuraciones en todas las cuentas
- Detecta desviaciones de políticas organizacionales
- Agrega resultados de auditoría multi-cuenta
- Se despliega centralizadamente desde Organizations

### CloudTrail
- Logging centralizado de todas las cuentas
- Auditoría de cambios en Organizations
- Trazabilidad de acciones entre cuentas
- Previene manipulación de logs con SCPs

### AWS Budgets
- Presupuestos a nivel de organización
- Monitoreo de costos agregados por OU
- Alertas de sobrecostos centralizadas
- Integración con Consolidated Billing

### Control Tower
- Usa Organizations como base
- Automatiza configuración de OUs y SCPs
- Añade Account Factory y guardrails
- Simplifica gestión de Organizations a gran escala

## Palabras Clave en Preguntas de Examen

Cuando veas estos términos, piensa en **AWS Organizations**:

- **Multi-cuenta** / Multi-account
- **Unidad organizacional** / OU
- **SCP** (Service Control Policy)
- **Políticas centralizadas**
- Consolidated Billing
- Facturación consolidada
- Gestión jerárquica
- Control de cuenta
- Políticas organizacionales
- Restricción de servicios por cuenta

## Comparación: Organizations vs IAM vs Control Tower

| Aspecto | Organizations | IAM | Control Tower |
|---------|---------------|-----|---------------|
| **Alcance** | Múltiples cuentas | Dentro de una cuenta | Múltiples cuentas (automatizado) |
| **Permisos** | Establece límites máximos (SCPs) | Otorga permisos específicos | Implementa políticas (usa Organizations) |
| **Nivel** | Organización/OU/Cuenta | Usuario/Rol/Grupo | Organización completa |
| **Facturación** | ✅ Consolidada | ❌ No aplica | ✅ Consolidada (heredado de Organizations) |
| **Complejidad** | Media (manual) | Baja (por recurso) | Alta (automatizado) |
| **Gestión** | Manual | Manual | Automatizada |
| **Landing Zone** | ❌ No incluye | ❌ No aplica | ✅ Automatizada |

**Relación clave:**
- **IAM**: Permisos dentro de una cuenta → "¿Qué puede hacer este usuario?"
- **Organizations**: Control entre cuentas → "¿Qué puede hacer esta cuenta completa?"
- **Control Tower**: Organizations + Automatización → "Gestiona Organizations automáticamente"

## Errores Comunes en el Examen

### ❌ Confundir Organizations con IAM
- **IAM**: Controla acceso **dentro** de una cuenta (usuarios, roles, grupos)
- **Organizations**: Controla acceso **de** cuentas completas (SCPs)
- IAM otorga permisos, Organizations los limita

### ❌ Asumir que Organizations controla por servicio, no por cuenta
- Organizations gestiona **cuentas**, no servicios individuales
- Para control granular de servicios dentro de una cuenta → IAM
- SCPs sí pueden restringir servicios, pero a nivel de cuenta/OU

### ❌ Pensar que SCPs otorgan permisos
- SCPs **NO otorgan** permisos, solo establecen límites
- Aún necesitas políticas IAM para dar acceso
- SCPs funcionan como filtro sobre permisos IAM

### ❌ No considerar herencia de SCPs
- SCPs se heredan desde el Root hacia OUs anidadas
- Un Deny en nivel superior no puede ser override en niveles inferiores
- Planifica estructura de OUs considerando herencia

## Arquitectura de AWS Organizations

### Cuenta de Management (Master Account)

#### Características
- Cuenta root que crea la organización
- Paga todas las facturas consolidadas
- Control completo sobre la organización
- Puede crear/eliminar cuentas miembro
- **No se debe usar para workloads**

#### Consideraciones de Seguridad
- Habilita MFA en cuenta root
- Restringe acceso a mínimos administradores
- No despliegues aplicaciones aquí
- Usa solo para gestión organizacional

### Cuentas Miembro

#### Creación
1. **Invitación**: Invitar cuenta AWS existente
2. **Creación**: Crear nueva cuenta desde Organizations
3. **Account Factory**: Usar Control Tower para automatización

#### Características
- Facturadas a través de la cuenta de management
- Sujetas a SCPs de su OU
- Pueden salir de la organización (si no están restringidas)
- Comparten descuentos y reservas con la organización

### Estructura Organizacional Típica

```
Root (Management Account)
│
├── Security OU
│   ├── SCP: Requiere MFA, cifrado obligatorio
│   ├── Log Archive Account
│   ├── Audit Account
│   └── Security Tools Account
│
├── Infrastructure OU
│   ├── SCP: Solo admins, regiones limitadas
│   ├── Shared Services Account
│   └── Network Account
│
├── Production OU
│   ├── SCP: No eliminar logs, restricciones estrictas
│   ├── Prod-App-A Account
│   └── Prod-App-B Account
│
├── Non-Production OU
│   │
│   ├── Development OU
│   │   ├── SCP: Restricción de tipos de instancia
│   │   └── Dev Team Accounts
│   │
│   └── Testing OU
│       ├── SCP: Apagado automático nocturno
│       └── Test Team Accounts
│
└── Sandbox OU
    ├── SCP: Sin acceso a producción, presupuesto limitado
    └── Experimental Accounts
```

## Facturación Consolidada (Consolidated Billing)

### Beneficios

#### Factura Única
- Una sola factura para todas las cuentas
- Simplifica contabilidad y pagos
- Facilita seguimiento de costos organizacional

#### Descuentos por Volumen Agregado
- Uso combinado de todas las cuentas
- Alcanza niveles de descuento más rápido
- Ahorro automático por economías de escala

**Ejemplo:**
```
Cuenta A: 400 GB S3 → $0.023/GB = $9.20
Cuenta B: 400 GB S3 → $0.023/GB = $9.20
Total separado: $18.40

Con Organizations (800 GB agregados):
Primeros 50 TB: $0.023/GB
Volumen agregado puede aplicar a tier con descuento
Total consolidado: ~$17.50 (ahorras $0.90)
```

#### Reservas e Instancias Compartidas
- Reserved Instances compartidas entre cuentas
- Savings Plans aplicados organizacionalmente
- Optimización automática de descuentos

#### Créditos Centralizados
- Créditos AWS se aplican a toda la organización
- Se usan automáticamente donde más beneficio
- Reduce complejidad de gestión de créditos

### Cost Allocation Tags

- Tags propagados desde cuentas miembro
- Reportes de costos por tag organizacional
- Facilita chargeback a departamentos
- Integra con Cost Explorer para análisis

## Tipos de Políticas en Organizations

### 1. Service Control Policies (SCPs)
**Propósito**: Controlar permisos máximos de cuentas
- Ya explicadas en detalle arriba
- Más comunes en exámenes

### 2. Tag Policies
**Propósito**: Estandarizar etiquetado de recursos
- Define tags requeridos (ej: "CostCenter", "Environment")
- Valida formato y valores de tags
- Genera reportes de cumplimiento
- Facilita gestión de costos y auditoría

**Ejemplo de uso:**
```json
{
  "tags": {
    "CostCenter": {
      "tag_key": "CostCenter",
      "enforced_for": {
        "ec2:instance": true
      }
    }
  }
}
```

### 3. Backup Policies
**Propósito**: Gestionar backups centralizadamente
- Define planes de backup obligatorios
- Aplica políticas de retención
- Asegura cumplimiento de DR (Disaster Recovery)
- Usa AWS Backup para implementación

### 4. AI Services Opt-out Policies
**Propósito**: Controlar uso de datos por servicios AI
- Previene que AWS use contenido para mejorar servicios
- Importante para cumplimiento regulatorio (GDPR, HIPAA)
- Aplica a Rekognition, Comprehend, etc.

## Mejores Prácticas

1. **Habilita MFA en la cuenta de Management**: Protege la cuenta root organizacional
2. **No uses la cuenta de Management para workloads**: Solo para gestión organizacional
3. **Diseña estructura de OUs antes de implementar**: Cambiar después es complejo
4. **Usa deny list por defecto**: Comienza con FullAWSAccess y niega específicamente
5. **Implementa SCPs progresivamente**: Evita bloqueos accidentales
6. **Combina con CloudTrail**: Auditoría completa de acciones organizacionales
7. **Documenta excepciones a SCPs**: Mantén registro de por qué se aplican políticas
8. **Usa Tag Policies**: Facilita gestión de costos y cumplimiento
9. **Planifica para crecimiento**: Diseña estructura escalable desde el inicio
10. **Considera Control Tower para automatización**: Si gestionas 10+ cuentas

## Limitaciones

- Máximo 5 niveles de anidamiento de OUs
- No puedes mover la cuenta de Management a otra organización
- Cuentas miembro solo pueden pertenecer a una organización
- SCPs no afectan usuarios IAM fuera de la cuenta (usuarios externos)
- Algunos servicios tienen límites específicos con Organizations
- Cambiar estructura de OUs puede requerir recrear políticas

## Pricing (Precios)

**AWS Organizations es completamente GRATUITO**

No hay cargos por:
- Crear una organización
- Agregar cuentas
- Aplicar SCPs
- Facturación consolidada
- Gestión de OUs

**Pagas solo por:**
- Recursos AWS desplegados en cada cuenta
- Servicios integrados (Config, CloudTrail, etc.)

## Comandos AWS CLI

```bash
# Crear organización
aws organizations create-organization

# Listar cuentas
aws organizations list-accounts

# Crear OU
aws organizations create-organizational-unit --parent-id r-xxxx --name "Production"

# Mover cuenta a OU
aws organizations move-account --account-id 123456789012 --source-parent-id r-xxxx --destination-parent-id ou-xxxx

# Listar SCPs
aws organizations list-policies --filter SERVICE_CONTROL_POLICY

# Adjuntar SCP a OU
aws organizations attach-policy --policy-id p-xxxx --target-id ou-xxxx

# Listar cuentas en OU
aws organizations list-accounts-for-parent --parent-id ou-xxxx

# Invitar cuenta existente
aws organizations invite-account-to-organization --target Id=123456789012,Type=ACCOUNT
```

## Escenarios de Examen SAA-C03

### Escenario 1: Restricción de Regiones
**Pregunta**: Una empresa necesita cumplir con regulaciones que requieren que todos los datos permanezcan en Europa. ¿Cómo prevenir que se lancen recursos fuera de eu-west-1 y eu-central-1?

**Respuesta**: Implementar SCP en el root de Organizations que deniegue todas las acciones en regiones fuera de las permitidas usando condición `aws:RequestedRegion`.

### Escenario 2: Descuentos por Volumen
**Pregunta**: Una empresa tiene 20 cuentas AWS, cada una con bajo uso individual. No califican para descuentos. ¿Cómo obtener descuentos por volumen agregado?

**Respuesta**: Consolidar cuentas en AWS Organizations con facturación consolidada para agregar uso y alcanzar niveles de descuento por volumen.

### Escenario 3: Prevenir Eliminación de Logs
**Pregunta**: Por requisitos de auditoría, los logs de CloudTrail no deben poder ser eliminados por ningún usuario, incluyendo administradores de cuenta.

**Respuesta**: Crear SCP a nivel de root que deniegue explícitamente las acciones `cloudtrail:DeleteTrail` y `cloudtrail:StopLogging` en todas las cuentas.

### Escenario 4: Políticas por Departamento
**Pregunta**: Los equipos de desarrollo y producción están en cuentas separadas. Desarrollo no debe acceder a RDS ni servicios de base de datos para controlar costos.

**Respuesta**: Crear Development OU con SCP que deniegue acciones sobre servicios RDS, DynamoDB, y otros servicios de bases de datos.

---

## Resumen Rápido para el Examen

**AWS Organizations = Gestión Multi-Cuenta Centralizada**

- ✅ **OUs**: Agrupan cuentas jerárquicamente
- ✅ **SCPs**: Establecen límites máximos de permisos (NO otorgan)
- ✅ **Consolidated Billing**: Factura única + descuentos agregados
- ✅ **Control Centralizado**: Políticas aplicadas desde un punto
- ✅ **Integración con Control Tower**: Organizations es la base
- ❌ **NO es IAM**: IAM controla dentro de cuenta, Organizations controla cuentas
- ❌ **NO es por servicio**: Es por cuenta completa

**Palabras clave**: multi-cuenta, OU, SCP, políticas centralizadas, facturación consolidada

**Relación con otros servicios:**
- Organizations < Control Tower (Control Tower usa Organizations)
- SCPs limitan ∩ IAM otorga = Permisos efectivos
- Organizations + Config + CloudTrail = Gobernanza completa

**Cuándo usarlo**: Múltiples cuentas AWS, necesidad de políticas centralizadas, consolidación de facturación, segregación organizacional.

# permite agruptar multipels cuentas WS
# Crear una cuenta de administracion / payer account
# habilitar facturacion consolodidada
# aplicar politicas centralizadas
# La cuenta dministrativa actua como pagador principal y puede ver los repotes de facturacion de todas las cuentas miembro
