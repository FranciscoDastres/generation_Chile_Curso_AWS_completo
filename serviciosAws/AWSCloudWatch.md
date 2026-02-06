# ☁️ AWS CloudWatch

## 📌 ¿Qué es CloudWatch?

**Amazon CloudWatch** es un servicio de monitoreo y observabilidad de AWS que permite **recopilar, visualizar y analizar métricas, logs y eventos** de los recursos que se ejecutan en la nube.

Su objetivo principal es ayudarte a **entender el estado, rendimiento y comportamiento** de tu infraestructura y aplicaciones, así como **detectar problemas y reaccionar automáticamente** ante ellos.

---

## 🎯 ¿Para qué sirve CloudWatch?

CloudWatch se utiliza principalmente para:

* 📊 **Monitorear recursos de AWS** (EC2, RDS, Lambda, ELB, ECS, etc.)
* 🧾 **Centralizar y analizar logs** de aplicaciones y sistemas
* ⏱️ **Medir rendimiento y uso** (CPU, memoria, red, latencia, errores)
* 🚨 **Crear alarmas automáticas** ante umbrales críticos
* ⚙️ **Automatizar acciones** (reiniciar instancias, escalar servicios, enviar notificaciones)
* 🔍 **Depurar y diagnosticar problemas** en producción

---

## 📊 Métricas (Metrics)

Las **métricas** son valores numéricos que representan el estado o rendimiento de un recurso.

### Ejemplos comunes

* Uso de CPU en EC2
* Lecturas/escrituras en RDS
* Número de requests en un Load Balancer
* Duración y errores en funciones Lambda

### Características

* Se recopilan automáticamente para muchos servicios AWS
* Se organizan por **Namespace**, **Métrica** y **Dimensiones**
* Se pueden visualizar en **gráficos y dashboards**

---

## 🧾 Logs (CloudWatch Logs)

CloudWatch Logs permite **almacenar, buscar y analizar logs** provenientes de:

* Instancias EC2
* Funciones Lambda
* Contenedores (ECS / EKS)
* Aplicaciones personalizadas

### Conceptos clave

* **Log Group**: conjunto de logs relacionados
* **Log Stream**: flujo de logs de una fuente específica

### Usos típicos

* Debug de errores
* Auditoría
* Análisis de comportamiento de aplicaciones

---

## 🚨 Alarmas (Alarms)

Las **alarmas** permiten definir reglas que se activan cuando una métrica cruza un umbral.

### Ejemplos

* CPU > 80% por 5 minutos
* Estado de instancia EC2 en `stopped`
* Errores Lambda > X

### Acciones posibles

* Enviar notificación (SNS / Email)
* Escalar automáticamente (Auto Scaling)
* Detener o reiniciar instancias

---

## 📈 Dashboards

Los **dashboards** son paneles visuales personalizables donde puedes:

* Ver múltiples métricas en tiempo real
* Centralizar información crítica
* Compartir vistas con tu equipo

Ideales para **monitoreo operativo y reportes rápidos**.

---

## ⚡ Eventos (CloudWatch Events / EventBridge)

Permite reaccionar a eventos que ocurren en AWS, como:

* Cambios de estado en EC2
* Ejecuciones de Lambda
* Errores en servicios

Se utiliza para **automatizar flujos** y **arquitecturas event-driven**.

---

## 🔐 Beneficios principales

* ✅ Monitoreo centralizado
* ✅ Alta integración con servicios AWS
* ✅ Escalabilidad automática
* ✅ Mejora la disponibilidad y confiabilidad
* ✅ Fundamental para entornos productivos

---

## 🧠 Resumen rápido

| Funcionalidad | ¿Para qué sirve?      |
| ------------- | --------------------- |
| Metrics       | Medir rendimiento     |
| Logs          | Analizar registros    |
| Alarms        | Alertar y automatizar |
| Dashboards    | Visualizar datos      |
| Events        | Reaccionar a eventos  |

---

## 📎 Recomendado para

* Proyectos en AWS
* Ambientes productivos
* Monitoreo DevOps
* Arquitecturas escalables

---

* Que es ?
# servicio de monitero y observabilidead e AWS
# monitorea recursos, app y servicios
# metrigas logs y alarmas

* sirve para
# monitorear perfomance
# ver metricas(cpu memoria request)
# centralizar logs
# crear alarmaas
# automatizar respuestas

# preguntas
 - una emopresa quiere recibir una alerta cuando la cpu supere 80%
 - cloud watch

 - una empresa quiere saber quien elimino una instancia
  # cloud trail
