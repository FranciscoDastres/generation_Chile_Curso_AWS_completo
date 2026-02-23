* Que es?
# es un framework ( guia de buenas practicas ) que sirve para diseñar, evaluar y mejorar arquitectura de AWS
# no es un servicio
# no se instala
# no cuesta dinero

*** es una checklist mental para saber si tu arquitectura esa bien hecha ***

* Para que sirve?
# sirve para detectar riesgos arquitectonicos
# mejorar seguridad, costos y rendimiento
# diseñar sistemas escalables y resilientes

* Pilares
# operational excellence como operas y mejoras el sistema
# seguridad → IAM encriptacion control de accesos deteccion de amenazas
# reliability → alta disponibilidad recuperacion ante fallos, backups,. multi AZ(multiples zonas de disponibilidad)
# perfonamce efficiencyy → que tan bien usas los recursos 
 - escalado automatico
 - servicos administrados
 - seleccion correcta de instancias
 # ejemplo 
  * lambda, auto scalling, graviton
# cost optimization → no gastar plata de mas , ppago por uso elminiacion de recursos ociosos right sizing (ajustar los recursos al tamaño correcto)

# sustentabilidad
 # uso eficiente de recursos
 # menos sobre aprovisionamiento
 # servicios administrados

* diferencia clave
# AWS CAF estrategia y adopcion
# Well Architected arquitectura tecnica

* Fiabilidad

# que el sistema noi se caiga
# que si algo falla se recupere solo


* pregunta examen
 # que principio de diseño de la nube de AWS pueden ayudar a aumentar la fiabilidad?
  - probar los procedimientos de recuperacion
   # Este principio forma parte del pilar de fiabilidad del marco de AWS Well-Architected. Cuando se prueban los procedimientos de recuperación, se validan los procedimientos para que pueda recuperarse de un error de manera fiable.
  - recuperacion automatica de errores 
   #  Este principio forma parte del pilar de fiabilidad del marco de AWS Well-Architected. En el evento en el que se detecte un error, se implementan procesos que pueden activarse sin intervención de manera manual. A esto se le llama recuperación automática de errores.