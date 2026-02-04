# Cuestionario AWS – IAM y Seguridad

Este documento contiene el cuestionario completo con **preguntas, opciones y respuestas correctas**, organizado en Markdown para estudio o repaso.

---

## Pregunta 1 – Escritorios virtuales

**Pregunta:** Una empresa quiere que sus empleados tengan acceso a la infraestructura de escritorios virtuales para acceder de forma segura a los escritorios que les proporcionan mediante los dispositivos personales de los empleados. ¿Qué servicio de AWS debería utilizar?

**Respuesta correcta:** ✅ **Amazon WorkSpaces**

Opciones:

* a. Amazon FSx para Windows File Server
* b. AWS AppSync
* c. Amazon WorkSpaces
* d. Amazon AppStream 2.0

---

## Pregunta 2 – Modelo de responsabilidad compartida

**Pregunta:** De acuerdo con el modelo de responsabilidad compartida de AWS, ¿cuál tarea es responsabilidad de AWS cuando se trata de cargas de trabajo que se ejecutan en Amazon EC2?

**Respuesta correcta:** ✅ **La actualización del hardware físico**

Opciones:

* a. La actualización del motor de base de datos
* b. La actualización del hardware físico
* c. La actualización del sistema operativo
* d. La actualización de los datos de usuario

---

## Pregunta 3 – Responsabilidad compartida

**Pregunta:** ¿Cuál es la responsabilidad compartida entre el usuario y los servicios de AWS?

**Respuesta correcta:** ✅ **Proveer información y formación**

Opciones:

* a. Configurar una instancia de Amazon EC2
* b. Proveer información y formación
* c. Proveer una clave para la encriptación del cliente de Amazon S3
* d. Controlar el entorno de los centros de datos físicos de AWS

---

## Pregunta 4 – Usuario raíz

**Pregunta:** ¿Cuál es una práctica recomendada de AWS para administrar un usuario raíz de una cuenta de AWS?

**Respuesta correcta:** ✅ **Utilizar la autenticación multifactor (MFA) para el usuario raíz**

Opciones:

* a. Utilizar la autenticación multifactor (MFA) para el usuario raíz
* b. No rotar la contraseña del usuario raíz
* c. Crear una clave de acceso para el usuario raíz
* d. Compartir la contraseña del usuario raíz con el equipo de operaciones

---

## Pregunta 5 – Control del tráfico de VPC (2 opciones)

**Pregunta:** ¿Cuáles servicios o funciones de AWS pueden controlar el tráfico de VPC?

**Respuestas correctas:** ✅ **Grupos de seguridad**, ✅ **Las ACL de red**

Opciones:

* a. AWS Direct Connect
* b. Amazon GuardDuty
* c. Las ACL de red
* d. Grupos de seguridad
* e. Amazon Connect

---

## Pregunta 6 – Usuarios y grupos IAM (2 opciones)

**Pregunta:** ¿Cuáles son características de los usuarios y los grupos de AWS IAM?

**Respuestas correctas:** ✅ **Un usuario puede ser miembro de diferentes grupos**, ✅ **Los grupos solo pueden contener usuarios y no se pueden anidar**

Opciones:

* a. Todos los usuarios nuevos se agregan automáticamente a un grupo predeterminado
* b. Un usuario solo puede ser miembro de un grupo a la vez
* c. Los grupos se pueden anidar y contener otros grupos
* d. Los grupos solo pueden contener usuarios y no se pueden anidar
* e. Un usuario puede ser miembro de diferentes grupos

---

## Pregunta 7 – Uso del usuario raíz (2 opciones)

**Pregunta:** ¿Qué tareas requieren el uso del usuario raíz de la cuenta de AWS?

**Respuestas correctas:** ✅ **Restaurar los permisos de administrador de IAM**, ✅ **Cerrar una cuenta de AWS**

Opciones:

* a. Ejecutar aplicaciones en Amazon EKS
* b. Restaurar los permisos de administrador de IAM
* c. Agrupar recursos en AWS Systems Manager
* d. Modificar un tipo de instancia de Amazon EC2
* e. Cerrar una cuenta de AWS

---

## Pregunta 8 – Acceso a AWS CLI

**Pregunta:** Un desarrollador debe acceder a los recursos de AWS desde AWS CLI. ¿Qué función de IAM puede usar para autenticarse?

**Respuesta correcta:** ✅ **Claves de acceso de IAM**

Opciones:

* a. Políticas de contraseña de la cuenta
* b. Políticas de IAM
* c. Claves de acceso de IAM
* d. Las claves SSH

---

## Pregunta 9 – Responsabilidad de AWS (2 opciones)

**Pregunta:** De acuerdo con el modelo de responsabilidad compartida de AWS, ¿cuáles son responsabilidad de AWS?

**Respuestas correctas:** ✅ **El parcheo y la actualización del hipervisor**, ✅ **La seguridad física de las instalaciones de AWS**

Opciones:

* a. El parcheo y la actualización del hipervisor
* b. El parcheo de sistemas operativos en EC2
* c. La encriptación de los datos de los clientes
* d. La seguridad física de las instalaciones de AWS
* e. La definición de firewalls de red dentro del servicio VPC

---

## Pregunta 10 – Responsabilidad del cliente (2 opciones)

**Pregunta:** De acuerdo con el modelo de responsabilidad compartida de AWS, ¿qué tareas son responsabilidad del cliente?

**Respuestas correctas:** ✅ **Aplicar parches al sistema operativo invitado**, ✅ **Configurar los firewalls**

Opciones:

* a. Proteger físicamente el hardware del centro de datos
* b. Aplicar parches al hardware de la red
* c. Desactivar los dispositivos de almacenamiento obsoletos
* d. Configurar los firewalls
* e. Aplicar parches al sistema operativo invitado

---

## Pregunta 11 – Seguridad del cliente (2 opciones)

**Pregunta:** ¿Qué tareas relacionadas con la seguridad son responsabilidad del cliente?

**Respuestas correctas:** ✅ **Encriptación de datos del lado del cliente**, ✅ **Integridad de datos del cliente**

Opciones:

* a. Seguridad de redes de infraestructura global de AWS
* b. Seguridad de las ubicaciones perimetrales
* c. Encriptación de datos del lado del cliente
* d. Seguridad del hardware en las regiones de AWS
* e. Integridad de datos del cliente

---

## Pregunta 12 – Claves de acceso del usuario raíz

**Pregunta:** ¿Cuál es una práctica recomendada de IAM para las claves de acceso del usuario raíz?

**Respuesta correcta:** ✅ **De ser posible eliminar todas las claves de acceso del usuario raíz**

Opciones:

* a. Utilizar credenciales de usuario raíz para acceder a información confidencial
* b. Utilizar credenciales de usuario raíz para bases de datos de producción
* c. De ser posible eliminar todas las claves de acceso del usuario raíz
* d. Permitir que el grupo de administradores use credenciales del usuario raíz para acceso diario

---

## Pregunta 13 – Buenas prácticas IAM (2 opciones)

**Pregunta:** ¿Cuáles son prácticas recomendadas de seguridad para usar IAM?

**Respuestas correctas:** ✅ **Rotar las credenciales con regularidad**, ✅ **Habilitar autenticación multifactor (MFA)**

Opciones:

* a. Utilizar políticas insertadas en lugar de políticas administradas por el cliente
* b. No eliminar credenciales aunque no se usen
* c. Utilizar credenciales de usuario raíz para tareas de IAM
* d. Rotar las credenciales con regularidad
* e. Habilitar MFA

---

## Pregunta 14 – Responsabilidad de AWS

**Pregunta:** ¿Cuál es una responsabilidad de AWS en el modelo de responsabilidad compartida?

**Respuesta correcta:** ✅ **Proteger la infraestructura física**

Opciones:

* a. Diseñar la aplicación de un cliente para recuperación ante desastres
* b. Actualizar sistemas operativos invitados en EC2
* c. Configurar nuevos recursos dentro de la cuenta de AWS
* d. Proteger la infraestructura física

---

## Pregunta 15 – Acceso a Secrets Manager

**Pregunta:** Una instancia de EC2 necesita acceder a AWS Secrets Manager para recuperar credenciales. ¿Qué necesita?

**Respuesta correcta:** ✅ **Rol de IAM**

Opciones:

* a. Grupo de seguridad
* b. Grupo de IAM
* c. Rol de IAM
* d. Autenticación multifactor (MFA)

---

## Pregunta 16 – Acceso remoto seguro a EC2

**Pregunta:** ¿Qué debe usar la empresa para acceder a instancias de EC2 sin abrir puertos SSH?

**Respuesta correcta:** ✅ **AWS Systems Manager Session Manager**

Opciones:

* a. Las ACL de red
* b. AWS Systems Manager Session Manager
* c. Pares de claves EC2
* d. IAM

---

## Pregunta 17 – Límite de servicio de VPC

**Pregunta:** ¿Qué servicio ayuda a determinar si se necesita un aumento del límite de servicio de VPC?

**Respuesta correcta:** ✅ **AWS Trusted Advisor**

Opciones:

* a. AWS Trusted Advisor
* b. AWS Cost and Usage Report
* c. AWS Health Dashboard
* d. AWS Service Catalog

---

📘 **Fin del cuestionario**
