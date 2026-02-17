* Que es? 
 # Es un servicio de CI/CD totalmen te administrado
 # Automatiza el proceso de build, test y deploy
 # Permite integrar código desde repositorio hasta producción
 # Es el " Flujo automático" que mueve tu código

* Para que sirve?
 # Para automatizar
  - Integración continua (CI)
  - Entrega continua (CD)
  - Deploy automático
  - Testing automático
  - Pipelines DevOps

* Ejemplos reales: 
 # Cada vez que haces push a GitHub → se ejecutan test → se despliega la app
 # Despliegue automático a EC2
 # Deploy a ECS o Lambda ( ECS= Amazon elastic Container Service = servicio para ejecutar y administrar contenedores en la nube(docker))
 # Pipeline para aplicacioens móviles o web

* Cómo funciona?
# Un pipeline tiene etapas(stages)  
 - 1 Source → Código (GitHub, CodeCommit)
 - 2 Build → Compilacion (CodeBuild)
 - 3 Test → Pruebas automáticas
 - 4 Deploy → Despliegue (Codeploy, ECS, Lambda)

* Caracteristicas importantes
 # Serverless
 # Integracion con GitHub y otros repositorios
 # Automatización completa
 # Reduce errores manuales
 # Soporta múltiples entornos (dev,staging,prod)
 # Staging: se refiere a un entorno intermedio donde se despliega y prueba una app antes de pasarla a prod, simula un entorno de produccion lo mas fielmente posible, para detectar errores, validar integraciones y asegurar caldiad de sw sin afectar a los usuarios finales

* Frase para memorizar 
 # CodePipeline = automatiza el flujo desde código hasta producción

* Necesitas automatizar build, test y deploy cuando hay cambios en el código
 # AWS CodePipeline

* Necesitas solo compilar código
 # AWS CodeBuild

* Necesitas solo hacer despliegues automatizados
 # AWS CodeDeploy


 # Pipeline = Orquesta
 # Build = Compila
 # Deploy = Despliega
 # Commit = Repo 

