* Que es?
 # una DB NoSQL, totalmente administrada por AWS, serverless, extremadamente rápida y escalable
 # no hay servidores
 # no hay parches
 # no hay mantenimiento
 # aws se encarga de todo

* para que sirve?
 # muchisimas lecturas/ esctrituras por segundo
 # baja latencia (milisegundos)
 # escalar automaticamente

 * ejemplos reales
 # juegos reales
 # carritos de compra
 # sesiones de usuarios
 # rankings
 # IOT
 # API BACKEND

* como funciona
 # dinamoDB guarda datos en tablas pero 
 - no usa SQL
 - usa clave primaria
 # tipos de clave primaria
 - partition Key (simple)
 - partition Key + Sort Key (compuesta)

 # es serverless , es un modelo donde no te preocupas por servidores pero si usas servidores
 # una app necesita millones de request por segundo baja latencia y escalado automatico sin administrar servidores
 # amazon dynamoDB