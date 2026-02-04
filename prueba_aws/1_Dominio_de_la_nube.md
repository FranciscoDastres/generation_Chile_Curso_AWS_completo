# 📘 Evaluación AWS – Preguntas, Respuestas y Justificación

---

## 🟢 Pregunta 1
**Desde múltiples recursos externos surgen ataques de inyección SQL dirigidos a una aplicación.  
¿Cuál servicio o función de AWS puede ayudar a automatizar la mitigación en contra de estos ataques?**

**Opciones:**
- a. AWS WAF ✅
- b. Grupos de seguridad
- c. ACL de red
- d. Elastic Load Balancing (ELB)

**Respuesta correcta:** ✅ **AWS WAF**

**Justificación:**  
AWS WAF (Web Application Firewall) protege aplicaciones web contra ataques comunes como **SQL Injection** y **XSS**, usando reglas administradas y personalizadas.

---

## 🟢 Pregunta 2
**Una empresa grande tiene una carga de trabajo que requiere que el hardware permanezca en las instalaciones.  
Desea utilizar los mismos servicios de plano de administración y control que utiliza en AWS.**

**Opciones:**
- a. AWS Device Farm
- b. AWS Outposts ✅
- c. AWS Fargate
- d. AWS Ground Station

**Respuesta correcta:** ✅ **AWS Outposts**

**Justificación:**  
AWS Outposts extiende la infraestructura y servicios de AWS a las instalaciones locales, manteniendo el mismo plano de control y administración.

---

## 🟢 Pregunta 3
**Una empresa tiene licencias de software que requieren núcleos físicos.  
¿Cómo puede cumplir este requisito en AWS?**

**Opciones:**
- a. Reserva de capacidad bajo demanda
- b. Instancias reservadas dedicadas
- c. Instancia EC2 en un servidor dedicado ✅
- d. Instancia EC2 con tenencia predeterminada

**Respuesta correcta:** ✅ **Instancia EC2 en un servidor dedicado**

**Justificación:**  
Los **Dedicated Hosts** permiten control sobre el hardware físico y cumplir requisitos de licenciamiento por núcleo.

---

## 🟢 Pregunta 4
**¿Qué servicio ofrece una forma sencilla de configurar un entorno de AWS con múltiples cuentas y gobernanza a escala?**

**Opciones:**
- a. AWS Control Tower ✅
- b. AWS Resource Access Manager
- c. AWS Trusted Advisor
- d. AWS Security Hub

**Respuesta correcta:** ✅ **AWS Control Tower**

**Justificación:**  
Automatiza la creación de cuentas, políticas, guardrails y gobernanza multi-cuenta.

---

## 🟢 Pregunta 5
**¿Qué servicio monitorea continuamente la actividad de cuentas de AWS (Consola, SDK y CLI)?**

**Opciones:**
- a. Amazon CloudWatch
- b. Amazon Inspector
- c. AWS CloudTrail ✅
- d. AWS Trusted Advisor

**Respuesta correcta:** ✅ **AWS CloudTrail**

**Justificación:**  
Registra todas las llamadas a la API y acciones realizadas en la cuenta.

---

## 🟢 Pregunta 6
**¿Qué servicios ayudan a proteger contra ataques DDoS? (Seleccione DOS)**

**Opciones:**
- a. Amazon CloudFront ✅
- b. AWS CloudTrail
- c. AWS Shield ✅
- d. AWS Support
- e. AWS Health Dashboard

**Respuestas correctas:**  
✅ **AWS Shield**  
✅ **Amazon CloudFront**

**Justificación:**  
Shield protege contra DDoS y CloudFront absorbe ataques mediante la red global.

---

## 🟢 Pregunta 7
**Un usuario debe migrar petabytes de datos desde un lugar sin buena conectividad.  
¿Cuál es el servicio MÁS RÁPIDO?**

**Opciones:**
- a. AWS Batch
- b. Amazon S3
- c. AWS VPN
- d. AWS Snowball Edge ✅

**Respuesta correcta:** ✅ **AWS Snowball Edge**

**Justificación:**  
Transferencia física segura y mucho más rápida que Internet.

---

## 🟢 Pregunta 8
**Una empresa necesita transferir 60 TB de datos a AWS de forma segura.**

**Opciones:**
- a. Amazon EBS
- b. Amazon S3
- c. Amazon EFS
- d. AWS Snowball Edge ✅

**Respuesta correcta:** ✅ **AWS Snowball Edge**

---

## 🟢 Pregunta 9
**Una empresa se traslada de oficina y necesita una conexión cifrada con AWS.**

**Opciones:**
- a. AWS Direct Connect
- b. Amazon Route 53
- c. Amazon Connect
- d. AWS VPN ✅

**Respuesta correcta:** ✅ **AWS VPN**

**Justificación:**  
VPN proporciona cifrado IPsec. Direct Connect no cifra por defecto.

---

## 🟢 Pregunta 10
**¿Cuál es un beneficio de usar servicios administrados de AWS?**

**Opciones:**
- a. Eliminar estándares de cumplimiento
- b. Eliminar backups
- c. Incrementar costos fijos
- d. Reducir sobrecarga operativa ✅

**Respuesta correcta:** ✅ **Reducir la sobrecarga operativa**

---

## 🟢 Pregunta 11
**¿Qué beneficio mejora el tiempo de comercialización al migrar a AWS?**

**Opciones:**
- a. Incrementar seguridad
- b. Incrementar respaldos
- c. Incrementar agilidad empresarial ✅
- d. Disminuir velocidad

**Respuesta correcta:** ✅ **Incrementar agilidad empresarial**

---

## 🟢 Pregunta 12
**¿Qué beneficio ofrece Amazon Rekognition?**

**Opciones:**
- a. Redimensionar imágenes
- b. Ofertar trabajos
- c. Detectar objetos en imágenes ✅
- d. Colocar marcas de agua

**Respuesta correcta:** ✅ **Detectar objetos en imágenes**

---

## 🟢 Pregunta 13
**Función básica del AWS CAF desde operaciones**

**Opciones:**
- a. Administrar productos
- b. Administrar cartera de aplicaciones
- c. Administrar identidades
- d. Administrar rendimiento y capacidad ✅

**Respuesta correcta:** ✅ **Administrar rendimiento y capacidad**

---

## 🟢 Pregunta 14
**Principio de diseño relacionado con redimensionamiento de infraestructura**

**Opciones:**
- a. Cambios pequeños
- b. Escalar horizontalmente
- c. Optimizar costos ✅
- d. Operaciones como código

**Respuesta correcta:** ✅ **Optimizar costos**

---

## 🟢 Pregunta 15
**Principios que aumentan la fiabilidad (Seleccione DOS)**

**Opciones:**
- a. Medir eficiencia
- b. Adoptar consumo
- c. Probar recuperación ✅
- d. Recuperación automática de errores ✅
- e. Arquitectura monolítica

---

## 🟢 Pregunta 16
**¿Qué servicio puede alojar un sitio web estático?**

**Opciones:**
- a. Amazon S3 ✅
- b. Amazon QuickSight
- c. AWS X-Ray
- d. Amazon Route 53

---

## 🟢 Pregunta 17
**¿Qué servicio migra una base de datos activa a AWS?**

**Opciones:**
- a. AWS DMS ✅
- b. AWS Application Migration Service
- c. AWS DataSync
- d. AWS Storage Gateway

---

## 🟢 Pregunta 18
**Un sistema se recupera automáticamente de un error.  
¿Qué pilar Well-Architected representa esto?**

**Opciones:**
- a. Fiabilidad ✅
- b. Eficiencia de rendimiento
- c. Excelencia operativa
- d. Optimización de costos

---

## 🟢 Pregunta 19
**Auditar recursos y documentar cambios**

**Opciones:**
- a. CloudWatch
- b. Inspector
- c. Artifact
- d. AWS Config ✅

---

## 🟢 Pregunta 20
**Acceso programático a servicios AWS**

**Opciones:**
- a. CodePipeline
- b. Consola AWS
- c. CodeDeploy
- d. AWS SDKs ✅

---

## 🟢 Pregunta 21
**Visualizar y analizar costos en el tiempo**

**Opciones:**
- a. Trusted Advisor
- b. Budgets
- c. Cost Explorer ✅
- d. CloudWatch

---

## 🟢 Pregunta 22
**Ejemplo de alta disponibilidad**

**Opciones:**
- a. Pago bajo demanda
- b. Aplicación accesible aunque falle un recurso ✅
- c. Implementación global
- d. Soporte 24/7

---

## 🟢 Pregunta 23
**Principios de seguridad Well-Architected (Seleccione DOS)**

**Opciones:**
- a. Proteger datos en tránsito y reposo ✅
- b. Monitorear y auditar acciones ✅
- c. Implementar globalmente
- d. Analizar gastos
- e. Operaciones como código

---

## 🟢 Pregunta 24
**Replicar datos entre áreas geográficas para DR**

**Opciones:**
- a. Cuentas
- b. Edge locations
- c. Regiones AWS ✅
- d. Zonas de disponibilidad

---

## 🟢 Pregunta 25
**Implementación automática de una app Java**

**Opciones:**
- a. AWS Elastic Beanstalk ✅
- b. Amazon EC2
- c. Auto Scaling
- d. Control Tower

---

## 🟢 Pregunta 26
**Características de regiones y AZ (Seleccione DOS)**

**Opciones:**
- a. Regiones llevan servicios on-prem
- b. Regiones en todo el mundo ✅
- c. Una AZ contiene varias regiones
- d. Regiones con múltiples AZ ✅
- e. Regiones separadas por 100 km

---
