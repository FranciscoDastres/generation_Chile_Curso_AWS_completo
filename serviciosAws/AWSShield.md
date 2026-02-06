* Que es?
# es un servicio de proteccion contra ataques DDOS
# Protege aplicaciones que corren en AWS

* Para que sirve
# detectar ataques DDos
# Mitigar ataques automáticamente
# Mantener disponibilidad de servicios

# Aplica a Cloudfront, Route 53 , ALB /NLB EC2

* Tipos de AWS Shield

* shield standar
 # proteccion basica de DDOS 
 # mitigacion atuomatica
 # no requiere configuracion
 # todos lo tienen 

* Shield  Advanced

 # proteccion avanzada
 # ddos response team 
 # soporte 24/7
 # proteccion de costos
 # Nivel enterprise

* Como funciona
 # detecta trafico anomalo ( deteccion de patrones fuera de lo normal, millones de request , muchas conexiones de ip etc)
 # mitiga automaticamente
 # (advanced) aws interviene activamente
 # mantioene la app disponible
 # es preventivo y reactivo

* Cuando usarlo
 # tu all es critica
 # no puedes permitir caidas
 # estas expuesto a internet
 # riesgo de ataques volumetricos
 # aplicacion publica necesita proteccion contra ataques DDoS

* cuando NO usarlo
 # filtra ataques a nivel de app
 # analizar logs
 # vulnerabilidades

 # no reemplaza , WAF guarduty , inspector

* SHIELD ES DDOS NADA MAS 
* una empresa requiere proteger su app web publica contra ataques de DDOS

# AWS SHIELD

# SHIELD = DDOS
# WAF = ATAQUES WEB
# GUARDDUTY = AMENAZAS
# INSPECTOR VULNERABILIDADES