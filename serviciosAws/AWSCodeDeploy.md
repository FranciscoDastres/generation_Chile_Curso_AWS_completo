* Qué es ?
 # Servicio que automatiza el despliegue de aplicaciones
 # Permite actualizar aplicaciones sin intervención manual
 # Parte del ecosistema CI/CD de AWS
 # Es el servicio que instala tu aplicación en los servidores

* Para que sirve? 
 # Para desplegar aplicaciones en: 
  - Amazon EC2
  - AMazon Lambda
  - Amazon ECS
  - Servidores on-premise

* Ejemplos reales:
 # Actualizar una aplicacion web en EC2
 # Desplegar una nueva version de una API ( forma estructura de permitir 2 sistemas que se comuniquen)
 # Hacer rollout gradual en una app (desplegar nueva version de una app en prod)
 # Actualizar una funcion Lambda automáticamente(funcion que se ejecuta sin que tengas que administrar servidores)  

* Conceptos extras:
 # API → Puerta de entrada para comunicación entre sistemas
 # Rollout → Forma en que publicas una nueva versión
 # Lambda → Código que se ejecuta automáticamente sin servidor 

* Como funciona?
 # 1-Recibe un artefacto(desde CodeBuild o S3)
 # 2-Usa un archivo llamado appspec.yml
 # 3-Ejecuta scripts antes, durante y despues del despliegue
 # 4-Instala la nueva versión

* Tipos de despliegue
 # In-place 
  - Actualiza los servidores existentes
  - Más simple
  - Puede haber pequeño downtime

 # Blue/Green
  - Crea un nuevo entorno
  - Cambia tráfico cuando está listo
  - Sin downtime
  - Más seguro

 # Blue/Green es común en preguntas de certificacion

* Características importantes
 # Despliegues automáticos
 # Rollback automático si falla
 # Integración con:
  - Codepipeline
  - CodeBuild
  - Auto Scalling
 # Reduce errores humanos

* Diferencia con otros servicios DevOps
 # CodeCommit → Guarda el código
 # CodeBuild → Compila y prueba
 # CodeDeploy → Despliega la aplicación
 # CodePipeline → Orquesta todo el proceso

* Frase para memorizar
 # CodeDeploy = instala y actualiza tu aplicación automáticamente

* Necesitas hacer despliegues automáticos en EC2
 # AWS CodeDeploy

* Necesitas despliegues sin downtime
 # CodeDeploy con Blue/Green

* Necesitas compilar código
 # CodeBuild