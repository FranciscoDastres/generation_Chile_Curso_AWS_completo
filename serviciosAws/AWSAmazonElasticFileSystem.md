* Que es ?
 # Servicio de sistema de archivos compartido
 # Totalmente administrado
 # Usa protocolos NFS (protocolo q permite compartir capretas y archivos a través de la red, como si estuvieran en su propio disco)
 # Compatible con Linux(POSIX) ( se comporta como un sistema linux tradicional y respeta el estandar posix)
 * Extra: 
  # Posix → Conjunto de reglas técnicas (estándares) que definen cómo debe comportarse un sistema operativo tipo Unix
  # Fue creado por el IEEE(Institute of Electrical and Electronics Engineers) para que los sitemas sean compatibles entre si
  # Define cómo deben funcionar:

  * Sistema de archivos
     # Permisos (r, w, x)
     # Usuarios (UID)
     # Grupos (GID)
     # Estructura de directorios

  * Procesos
     # Creación de procesos (fork)
     # Ejecución de programas (exec)
     # Señales (kill)

  * APIs del sistema
     # Funciones en C como open(), read(), write()

* Para que sirve     
 # Compartir archivos entre múltiples instancias EC2
 # Aplicaciones Linux que necesitan almacenamiento compartido
 # Sistemas CMS (WordPress, Drupal)
 # Contenedores que necesitan almacenamiento común
 # Home directories compartidos

* Ejemplos reales
 # Varias EC2 detras de un Load Balancer comparten archivos
 # Servidores web que necesitan acceso a las mismas imágenes
 # Aplicación que escala automáticamente y necesita datos compartidos
 # Cluster Linux con almacenamiento común

* Como funciona?
 # Creas un sistema de archivos EFS
 # Lo montas en multiples instancias EC2
 # Todas pueden leer y escribir al mismo tiempo
 # Escala automáticamente en tamaño

 # Características imortantes
  - Serverless
  - Escala automáticamente
  - Multi AZ (Alta disponibilidad)
  - Pago por uso
  - Integración con:
   - EC2
   - ECS
   - EKS
   - Lambda (soporte reciente)
 # EFS = carpeta compartida Linux en AWS

 # Necesitas almacenamiento compartido entre múltiples instancias EC2 Linux
 * Amazon EFS

 # Necesitas almacenamiento persistente para una sola instancia
 * EBS

 # Necesitas sistema de archivos Windows con Active Directory
 * FSx for Windows  

# Clases de almacenamiento en EFS

 * EFS Standard
  # Guarda datos en múltiples AZ
  # Alta disponibilidad
  # Más caro
  # Para datos activos y críticos
  # Producción , apps importantes, datos que no pueden perderse

 * EFS Standar-IA (Infrequent Access)
  # Más barato
  # Para datos que se usan poco
  # Multi AZ 
  # Se paga pequeño costo por acceso
  # Archivos que no se consultan frecuentemente

 * EFS One Zone
  # Guarda datos en una sola AZ
  # Más barato
  # Menor durabilidad
  # No es Multi-AZ

# Modos de rendimiento (Perfomance Modes)
 # General Purpose (predeterminado)
 - Baja latencia
 - Mejor para la mayoría de aplicaciones
 - Ideal para:
  - Web apps
  - CMS : significa Content Management System (Sistema de Gestión de Contenido)
  - Aplicaciones comunes
 # Es el modo recomendado normalmente 
 
 # Max I/O
 # Mas Throughput : cantidad de datos que se pueden transmitir o procesar en un periodo de tiempo 
  - Soporta altisima concurrencia
  - Mayor latencia
  - Ideal para:
   - Big Data
   - HPC (High Performance Computing (Computación de Alto Rendimiento))
   - Procesamientio masivo