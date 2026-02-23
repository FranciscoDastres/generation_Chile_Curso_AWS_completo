# servicio Paas que permite desplegar aplicacioens sin preocuparte por la infraestructura
# tu subes el codigo
# AWS maneja EC2, ELB, Auto scaling , monitoreo

- AWS Elastic Beanstalk permite desplegar y administrar aplicaciones sin gestionar la infraestructura subyacente.

# Elastic Beanstalk implementa y escala aplicaciones y servicios web. Primero, se debe cargar el código para Elastic Beanstalk. A continuación, Elastic Beanstalk administra automáticamente la implementación. Además, Elastic Beanstalk administra el aprovisionamiento de capacidad, el balanceo de carga, el escalado automático y el monitoreo del estado de las aplicaciones.

# si pregunta menciona 
 # implementacion automatica
 # crear entorno automaticamente
 # Aplicacion web java
 # Casi siempre es elastic beanstalk

# | Caso                                      | Servicio correcto   |
# | ----------------------------------------- | ------------------- |
# | App web Java con despliegue automático    | ✅ Elastic Beanstalk |
# | App frontend React con backend serverless | ✅ Amplify           |
# | Control total de infraestructura          | EC2                 |
# | Solo escalado automático                  | Auto Scaling        |
