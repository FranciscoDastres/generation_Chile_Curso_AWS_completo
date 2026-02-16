* Que es ? 
 # Amazon Elastic Comnpute Cloud  
 # Servicio que permite crear servidores virtuales en la nube
 # Proporciona capacidad de cómputo escalable
 # Tú eliges CPU, Ram, almacenamiento y red
 # Es básicamente alquilar un servidor en AWS

* Para que sirve?
 # Ejecuta: 
  - Aplicaciones Web
  - APis
  - Bases de datos
  - Aplicaciones empresariales
  - Sistemas Legancy
 # Ejemplos reales:
  - Un servidor Apache o Nginx
  - Una app backend en Node.js
  - Un servidor Windows empresarial 
  - Un servidor de Minecraft

* Como funciona
 # Eliges una AMI (Amazon Machine Image)  
 # Seleccionas tipo de instancia (CPU y RAM)
 # Configuras red y seguridad
 # Lanzas la instancia
 # Obtienes una máquina virtual lista para usar

* Tipos de instancias
 # General purpose → uso balanceado (t3,t4g,m5) 
 # Compute OPtimized → más CPU (c5)
 # Memory Optimized → más RAM (r5)
 # Storage Optimized
 # GPU instances → ML, IA, render

* Caracteristicas Importantes
 # Escalable
 # Pago por uso
 # Control total del sistema operativo
 # Integración con:
  # EBS(disco)
  # Security Groups
  # Auto Scaling
  # Load Balancer

* Modos de pago
 # On-demand
 # Reserved
 # Sport
 # Savings Plans

* Diferencias con otros servicios
 # EC2 → tú administras el servidor
 # Lambda → serverless (no administras servidores)
 # Elastic Beanstalk → despliegue automático de apps
 # Fargate → contenedores sin manejar servidores

* Frase para memorizar
# EC2 = servidor virtual en la nube

* Necesitas control total del sistema operativo
# EC2

* Necesitas código sin administrar servidores
# AWS Lambda

* Necesitas levantar una VM Windows en la nube
# EC2 