# Amazon CloudFront

## 📌 ¿Qué es Amazon CloudFront?

**Amazon CloudFront** es un **servicio de red de entrega de contenido (CDN, Content Delivery Network)** que entrega datos, videos, aplicaciones y APIs a los usuarios de forma **segura y con baja latencia**, aprovechando la infraestructura global de AWS.

CloudFront se utiliza para mejorar la **velocidad de entrega** y la **seguridad** de los contenidos que se sirven desde servicios como Amazon S3, servidores web o aplicaciones dinámicas.

---

## 🌍 Características principales

- **Entrega de contenido global**: CloudFront utiliza una red de **puntos de presencia (PoPs)** distribuidos mundialmente.
- **Optimización de rendimiento**: reduce la latencia al acercar los datos al usuario final.
- **Soporte para contenido dinámico y estático**: entrega imágenes, videos, archivos estáticos y APIs.
- **Seguridad integrada**: soporte de **AWS Shield, AWS WAF, SSL/TLS**, control de acceso y protección DDoS.
- **Integración con otros servicios AWS**: S3, EC2, Lambda@Edge, API Gateway.

---

## ⚙️ Cómo funciona CloudFront

1. El contenido se almacena en **orígenes**: S3, EC2, Elastic Load Balancer, etc.
2. CloudFront distribuye el contenido a **edge locations** cercanas al usuario final.
3. Cuando un usuario solicita un contenido:
   - Si el contenido está en caché en un edge location → se entrega directamente.
   - Si no está en caché → CloudFront lo obtiene del origen, lo entrega y lo almacena en caché.

---

## 🔧 Funcionalidades clave

- **Caché de contenido**: almacenamiento temporal en edge locations para acelerar la entrega.
- **Invalidación de caché**: permite actualizar contenido en los edge locations.
- **Soporte para HTTP/HTTPS**: entrega segura de contenido.
- **Lambda@Edge**: ejecución de funciones serverless en la red de CloudFront.
- **Compresión automática**: reduce el tamaño de los datos transferidos.

---

## 💡 Casos de uso comunes

- ✅ Distribución de sitios web estáticos y dinámicos
- ✅ Streaming de video y audio en tiempo real
- ✅ Aceleración de APIs
- ✅ Entrega segura de aplicaciones web
- ✅ Reducción de carga en servidores de origen

---

## 💰 Modelo de costos

Amazon CloudFront cobra según:
- Cantidad de **datos transferidos**
- Número de **solicitudes** al servicio
- Uso de **funciones Lambda@Edge** (si aplica)

---

## 🚀 Integración con otros servicios AWS

- **Amazon S3** → almacenamiento de contenido estático
- **Elastic Load Balancer / EC2** → origen de contenido dinámico
- **AWS WAF** → protección de aplicaciones web
- **Lambda@Edge** → lógica personalizada en la CDN

---

## 📝 Resumen

**Amazon CloudFront** es un servicio de **CDN** que permite:

> 🌍 Mejorar la velocidad y disponibilidad del contenido  
> 🔐 Proteger datos y aplicaciones  
> ⚡ Optimizar la experiencia de usuario final

Ideal para **sitios web, aplicaciones y APIs** que necesitan **rendimiento global y seguridad**.

---

📁 *Documento para repositorios, documentación interna o apuntes de certificación AWS.*

