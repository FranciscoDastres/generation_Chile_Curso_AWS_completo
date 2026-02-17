* Qué es?
 # Un servicio de repositorio Git totalmente administrado
 # Seguro y privado
 # Alternativa a GitHub o GitLab dentro de AWS
 # Es dónde guardas tu código fuente

* Para qué sirve?
 # Alamacenar código fuente
 # Control de versiones
 # Trabajo colabotarivo
 # Integrarse con pipelines CI/CD
 
* Ejemplos reales 
 # Equipo de desarrollo sube código a un repo privado
 # Proyecto empresarial que no puede usar GitHub público
 # Repositorio interno conectado a CodePipeline

* Cómo funciona?
 # Es compatible con Git estándar
 # Puedes hacer: 
  - git clone
  - git push
  - git pull
 # Se integra  con IAM para control de acceso
 # Puede activar automáticamente CodePipeline 

* Flujo típico:
 # Desarrollador → CodeCommit → CodePipeline → CodeBuild → Deploy

* Características importantes
 # Totalmente administrado
 # Alta disponibilidad
 # Integración con IAM
 # Encriptación automática
 # Sin servidores que administrar

* Diferencias con otros servicios DevOps
 # CodeCommit → Guarda el código (Repo)
 # CodeBuild → Compila y prueba
 # CodeDeploy → Despliega
 # CodePipeline → Orquesta todo el flujo

* Frase para memorizar
 # CodeCommit = repositorio de Git privado en AWS 

* Necesitas un Git privado dentro de AWS
 # AWS CodeCommit

* Necesitas automatizar el flujo copleto de CI/CD
 # AAWS CodePipeline

* Necesitas compilar código automáticamente
 # CodeBuild