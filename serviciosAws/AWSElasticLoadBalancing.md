* Que es?
 # Es un servicio que distribuye automaticamente el trafico entrante entre multiples recursos ( como instancias EC2)
 # Evita que un solo servidor se sobrecargue

* Para que sirve?
 # Alta disponibilidad
 # Escalabilidad automatica
 # Distribucion de tráfico
 # Tolerancia a fallos

* Como funciona
 # Los usuarios envian tráfioco a un load balancer
 # ELB distribuye las solicitudes entre múltiples servidores
 # Si un servidor falla → deja de enviarle tráfico
 # Hace health checks automáticos

* Tipos de Load Balancer
 # Application Load Balancer (ALB)
   - Capa 7 (HTTP/HTTPS)
   - Ideal para aplicaciones web
   - Soporta microservicios
   - Routing basado en URL
   - EJ:/api → servidor A / images → servidor B

 # Network Load Balancer (NLB)
  - Capa 4 (TCP/UDP)
  - Ultra baja latencia
  - Alto rendimiento
  - Soporta millones de solicitudes por segundo
  - Ideal para gaming o aplicaciones financieras

 # Gateway Load Balancer (GWLB)
  - Distribuye tráfico hacia appliances de seguridad (SEVIODOR O SOFTWARE ESPECIALIZADO QUE HACE UNA FUNCION DE RED O SEGURIDAD)    
  - FIrewalls
  - IDS/ IPS (INTRUSION DETECTION SYSTEM / IPS INTRUSION PREVENTION SISTEM)
  
 # ELB + Auto scaling 
  - Se integra con:
   # Amazon EC2
   # Amazon EC2 Auto Scaling
 # Cuando aumentan usuarios → Auto scalling crea mas instancia → ELB distruye el trafico

 # Cuando usar ELB 
  # apps web
  # alta disponibilidad
  # Arquitectura escalable
  # Microservicios

* Una empresa necesita distrbuir trafico HTTP entre múltiples instancias EC2 y enrutar según la URL
 # Application Load Balancer

* ELB = distribuye tráfico y mejora disponibilidad