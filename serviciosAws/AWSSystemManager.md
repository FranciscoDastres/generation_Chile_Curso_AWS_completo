* Que es ?
# es una funcionalidad de AWS System Manager que permite conectarse a instancias EC2 sin usar SSH RDP ni par de claves
# acceso 100% desde AWS Console o AWS CLI
# conexion segura y auditada

# servicio que permite administrar y operar recursos de AWS de forma centralizada (principalmente EC2)
# que significa que sea centralizada
 - que todo se controla o administra desde un unico punto o sistema princiupal en lugar ede estar distribuido en varios lugares independientes
 - Un solo servidor que controla todos los accesos → sistema centralizado
 - Cada departamento maneja su propio servidor → sistema decentralizado

# Gestion operativa sin necesidad de conectarme manualmente a cada servidor

* Para que sirve ?
 # Administrar instancias EC2
 # Ejecutar comandos remotamente
 # Aplicar parches
 # Automatizar tareas
 # Gestioanr configuraciones
 # Mantener inventario de servidores

 * Para que sirve? 
  # Administrar instancias EC2
  # Ejecutar comandos remotamente
  # Aplicar parches
  # Automatizar tareas
  # Gestionar configuraciones
  # Mantener inventario de servidores

  * Componentes de System manager
  # Session manager : Acceso remoto seguro ( SIN SSH NI BASTION HOST)
  # Run command : Ejecutar comandos en multiples instancias
  # Patch manager : Aplicar parches automaticamente
  # Parameter Store : Guardar variables y secretos
  # Automation : Automatiza tareas operativas

  * Requisitos clave : 
   # instancia EC2 con IAM Role
   # SSM Agent instalado
   # Acceso a internet o VPC Endpoint
  
# Se necesita acceso seguro a instancias en una subred privada sin abrir puertos entrantes.

*  Respuesta: Session Manager
 # System manager = administracion centralizada
 # Session manager Acceso seguro sin SSH