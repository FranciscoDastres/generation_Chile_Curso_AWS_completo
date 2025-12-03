# 🛡️ AWS Trusted Advisor – Guía Completa

Trusted Advisor ofrece prácticas recomendadas y verificaciones automáticas en cinco categorías principales para ayudarte a optimizar, proteger y monitorear tu infraestructura en AWS.

---

# ✔️ Estados de Seguridad

- 🟢 **Verde:** No se detectaron problemas.  
- 🟡 **Amarillo:** Se recomienda investigar.  
- 🔴 **Rojo:** Se recomienda tomar medidas inmediatas.

---

# 🚀 Uso de AWS Trusted Advisor

## Seis verificaciones básicas disponibles para todos los clientes

- **Service Limits**
- **Grupos de seguridad:** puertos específicos sin restricciones
- **Uso de AWS Identity and Access Management (IAM)**
- **Autenticación multifactor (MFA) en la cuenta raíz**
- **Instantáneas públicas de Amazon Elastic Block Store (EBS)**
- **Instantáneas públicas en Amazon Relational Database Service (RDS)**

---

# 🧩 Características de Trusted Advisor

Trusted Advisor proporciona funciones para personalizar recomendaciones y monitorear recursos de manera proactiva:

- **Notificaciones**
- **Administración de acceso**
- **API de AWS Support**
- **Enlaces de acción**
- **Cambios recientes**
- **Exclusión de elementos**
- **Actualización cada 5 minutos**

---

# 🔍 Categorías de recomendaciones de AWS Trusted Advisor

- **Optimización de costos**  
- **Rendimiento**  
- **Seguridad**  
- **Tolerancia a errores**  
- **Límites de servicio (Service Limits)**  

---

# 🔐 MFA en la cuenta raíz

## Descripción
Trusted Advisor verifica si la cuenta raíz tiene habilitada la autenticación multifactor (MFA).  
Habilitar MFA aumenta la seguridad al requerir un código único generado desde un dispositivo físico o virtual para acceder a la consola de AWS.

## Criterios de alerta
- 🔴 **La MFA no está habilitada en la cuenta raíz.**

## Acción recomendada
- Inicie sesión con la cuenta raíz y active un dispositivo MFA para proteger el acceso administrativo de mayor privilegio.

---

# 🛡️ Recomendaciones de Seguridad Avanzadas

## 🔐 Recomendación Nº 2  
## Política de contraseñas de IAM

### Descripción
Trusted Advisor verifica si la política de contraseñas cumple requisitos mínimos de complejidad o si no existe una política habilitada.  
Una política robusta mejora la seguridad del entorno AWS.

> **Nota:** Los cambios se aplican inmediatamente a nuevos usuarios, pero no obligan a los actuales a cambiar la contraseña.

### Criterios de alerta
- Hay una política de contraseñas, pero falta al menos un requisito de complejidad.
- No existe ninguna política configurada.

### Acción recomendada
- Habilitar los requisitos de contenido faltantes.
- Crear una política si aún no existe.
- Consultar la guía oficial: *"Configuración de una política de contraseñas de cuenta para usuarios de IAM"*.

---

## 🔒 Recomendación Nº 3  
## Grupos de Seguridad: Acceso Ilimitado

### Descripción
Esta verificación detecta reglas que permiten acceso desde **0.0.0.0/0**, un riesgo importante que puede permitir ataques, filtraciones y accesos no autorizados.

### Criterios de alerta
- Se detecta tráfico permitido desde **0.0.0.0/0** hacia cualquier puerto excepto **25, 80 o 443**.

### Acción recomendada
- Limitar acceso solo a IPs necesarias.
- Utilizar máscara **/32** para permitir una IP específica (ej.: `192.0.2.10/32`).
- Eliminar reglas demasiado permisivas tras agregar reglas más seguras.

### Ejemplos
| Región      | SG Name         | ID           | Protocolo | Puerto | Estado | Rango de IP |
|-------------|-----------------|--------------|-----------|--------|--------|-------------|
| us-east-1   | WebServerSG     | sg-xxxxxxx1  | tcp       | 22     | 🔴 Red | 0.0.0.0/0   |
| us-west-2   | DatabaseSG      | sg-xxxxxxx2  | tcp       | 8080   | 🔴 Red | 0.0.0.0/0   |

---

## 📦 Recomendación Nº 4  
## Registro de Buckets de Amazon S3

### Descripción
Verifica si los buckets tienen habilitado el **Server Access Logging**, que permite auditorías detalladas y análisis de uso.  
De forma predeterminada, este registro está deshabilitado.

### Criterios de alerta
- 🟡 El bucket no tiene habilitado el registro.
- 🟡 Trusted Advisor no puede verificar permisos porque la cuenta propietaria no está incluida.

### Acción recomendada
- Habilitar el registro en la mayoría de los buckets.
- Agregar la cuenta propietaria al bucket de destino si se requiere verificación automática.

### Ejemplo
| Región      | Bucket                 | Destino | Existe Destino | Propietario | Escritura | Razón                       |
|-------------|-------------------------|---------|-----------------|-------------|-----------|------------------------------|
| us-east-2   | my-hello-world-bucket   | No      | No              | No          | No        | Registro no habilitado       |

---

# 📌 Conclusiones

- **AWS Trusted Advisor** ayuda a mejorar seguridad, rendimiento y control de costos en tiempo real.
- Principales prácticas de seguridad:
  - Evitar puertos abiertos al público.
  - Revisar permisos de IAM y roles.
  - Habilitar MFA en la cuenta raíz.
  - Registrar el acceso a buckets S3 para auditorías.

