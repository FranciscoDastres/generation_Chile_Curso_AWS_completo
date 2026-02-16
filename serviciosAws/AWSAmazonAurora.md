# Amazon Aurora

## 📌 ¿Qué es Amazon Aurora?

**Amazon Aurora** es un **servicio de base de datos relacional** de AWS, compatible con **MySQL y PostgreSQL**, diseñado para ofrecer **alto rendimiento, disponibilidad y escalabilidad**, con la seguridad y confiabilidad de la nube de AWS.

Aurora combina la facilidad de uso de las bases de datos tradicionales con mejoras propias de AWS para **rendimiento y resiliencia**.

---

## ⚡ Características principales

- **Compatibilidad**: MySQL y PostgreSQL.
- **Alto rendimiento**: hasta 5 veces más rápido que MySQL estándar y 3 veces más rápido que PostgreSQL estándar.
- **Alta disponibilidad y recuperación automática**: replicación automática entre múltiples zonas de disponibilidad (AZ).
- **Escalabilidad**: capacidad de escalar almacenamiento automáticamente hasta 128 TB.
- **Seguridad**: cifrado de datos en reposo y en tránsito, integración con AWS IAM y KMS.
- **Backups automáticos**: respaldos continuos en Amazon S3.

---

## 🔧 Funcionalidades clave

- **Replica Aurora**: permite tener múltiples réplicas de lectura para mejorar rendimiento.
- **Aurora Serverless**: versión que escala automáticamente según la demanda, ideal para cargas variables.
- **Punto en el tiempo de recuperación (PITR)**: permite restaurar la base de datos a un momento específico.
- **Integración con otros servicios AWS**: CloudWatch (monitoreo), Lambda (triggers), VPC (seguridad de red).

---

## 💡 Casos de uso comunes

- ✅ Aplicaciones web y móviles de alta demanda
- ✅ Sistemas ERP y CRM en la nube
- ✅ Aplicaciones que requieren alta disponibilidad y replicación
- ✅ Cargas de trabajo con picos variables (usando Aurora Serverless)
- ✅ Migración desde MySQL o PostgreSQL con mínimo esfuerzo

---

## 💰 Modelo de costos

Amazon Aurora cobra según:
- **Instancias de base de datos** (tipo y cantidad)
- **Almacenamiento utilizado**
- **I/O consumido**
- **Backups adicionales y snapshots**

💡 Recomendación: seleccionar instancias y configuraciones adecuadas para optimizar costos.

---

## 🚀 Integración con otros servicios AWS

- **Amazon S3** → import/export de datos y backups
- **AWS Lambda** → triggers y lógica serverless
- **CloudWatch** → monitoreo y alertas
- **VPC** → aislamiento de red y seguridad
- **IAM & KMS** → gestión de acceso y cifrado

---

## 📝 Resumen

**Amazon Aurora** es una base de datos relacional **alta disponibilidad, escalable y segura**, compatible con MySQL y PostgreSQL, ideal para aplicaciones empresariales y cargas de trabajo críticas en la nube.

> ⚡ Alto rendimiento
> 🔐 Seguridad y cifrado
> 🌍 Alta disponibilidad y recuperación automática
