* Que es ? 
 # Un servicio serverless de compilacion (build)
 # Compila código, ejecuta pruebas y genera artefactos ( resultados de procesos de construccion(build))
 # Parte del ecosistema DevOps de AWS
 # Es el servicio que construye y prueba tu código automáticamente

* Para que sirve?
 # Compilar aplicaciones
 # Ejecutar pruebas unitarias
 # Generar Paquetes (Artefactos)
 # Construir imagenes Docker
 # Preparar código para despliegue

* Ejemplos reales:
 # Compilar una app java con Maven
 # Ejecutar test en una app Node.js
 # Construir una imagen Docker y subirla a ECR
 # Generar un archivo .zip para Lambda

* Como funciona? 
 - 1 se conecta al repositorio (Github, CodeCommit)
 - 2 Usa un archivo llamado buildspec.yml
 - 3 Ejecuta comandos definidos por ti
 - 4 Genera artefactos
 - 5 Puede integrarse con CodePipeline

# Ejemplo de flujo
  - Código → Codebuild → Artefacto → CodeDeploy

* Que es buildspec.yml= 
 # Es un archivo donde defines:
  - Fase instalacion
  - Fase de build
  - Fase de test
  - Artefactos a generar
 # Es como un "Script automático" de compilación

* Características importantes
 # Serverless
 # Escalable automáticamente
 # Paga solo por minutos de build
 # Soporta múltiples lenguajes
 # Puede usar contenedores Docker

* Diferencia entre otros servicios
 # Codebuild → compila y ejecuta test
 # Codedeploy → Despliega aplicaciones
 # CodePipeline → Orquesta todo el proceso
 # CodeCommit → Repositorio Git 

* Frase para memorizar
 # Codebuild = compila y prueba tu código automáticamente

* Necesitas compilar código y ejecutar pruebas automáticamente
# AWS Codebuild

* Necesitas automatizar todo el flujo CI/CD
 # AWS Codepipeline

* Necesitas desplegar una aplicación en EC2
 # AWS CodeDeploy