  * que es ? 
# es un CDN ( content delivery netfwork ) de AWS
# distribuye contenido desde ubicaciones cercanas al usuario

* para que sirve?
# reducir latencia
# mejorar rendimiento
# aumentar disponibilidad
# proteger app publicas
# distribuye
 * contenido estatico ( img, videos,js)
 * contenido dinamico
 * APis

* como funciona
# el usuario solicita contenido
# cloudfront responde desde la edge location mas cercana
# sino existe lo trae del origin(s3 , ALB,EC2), lo cachea, 
# lo entrega al usuario
# menos distancia = mas velocidad

* cuando usarlo 
# tu app es global
# tienes usuarios en varias regiones
# necesitas baja latencia
# quieres proteger tus servicios backend

* ejemplo examen
# empresa con usuarios globales quiere mejorar latencia y disponiblidad
# cloundfront

# CloudFront reduce el impacto de un ataque DDoS al distribuir y absorber las solicitudes en sus edge locations, de modo que muchas no llegan al backend.