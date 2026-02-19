* Que es ?
# un servicio de almacenamiento en bloques
# Se usa principalmente con instancias EC2
# Funciona como si fuera un disco duro virtual
# Es el disco de tu servidor de la nube

* Para que sirve?
# Para almacenar: 
 - Sistema operativo de EC2
 - Aplicaciones
 - Bases de datos
 - Archivos persistentes
 - Datos que necesitan baja latencai

# Ejemplos reales:
 - Un servidor Linux en EC2 necesita disco para instalar Apache
 - Una base de datos MYSQL corriendo en EC2
 - Aplicaciones empresariales que requieren almacenamiento persistente
 - Un servidor Windows con disco C: en la nube

* Como funciona?
# Se crea un volumen EBS
# Se adjunta instancia EC2
# EC2 lo ve como un disco normal
# Los datos persisten aunque la instancia se detenga
# Pero esta limitado a una zona de disponibilidad (AZ)

* Tipos de volúmenes
# SSD (para rendimiento alto)
 - gp3 (General Purpose → recomendado)

# HDD (para grandes volumenes)
 - st1(Troughput optimizado)
 - sc1(Cold HDD → más barato)
 
* Caracteristicas importantes
 # persistente (no se borra al apagar EC2)
 # Baja latencia
 # Se puede hacer snapshot a S3
 # Encriptacion disponible
 # Escalable (puedes aumentar tamaño)

* Limitaciones
 # Solo se puede adjuntar a EC2
 # Vive en una sola AZ
 # No es compartido por multiples instancias ( excepto configuraciones eespeciales como Multi-Attach)

* Diferencias con otros storage
# EBS → Disco para Ec2 (block storage)
# S3 → Almacenamiento de objetos
# EFS → Sistema de archivos comaprtido
# Instance Store → Temmporal (se piede al apagar)

* Frase para memorizar
# EBS = disco duro persistente para EC2

* Preguntas tipo examen 
# Necesitas almacenamiento persistente para una instancia EC2
# amazon EBS

# Necesitas un sistema de archivos comaprtido entre varias instancias EC2
# Amazon EFS 

# Necesitas almacenar backups y archivos estaticos
# Amazon S3