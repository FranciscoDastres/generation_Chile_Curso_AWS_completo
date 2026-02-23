# AWS Es responsable de la seguridad DE la nube, el cliente es responsable de la seguridad EN la nube

# quien es el responsable de parchar sistema operativo en una instancia ec2
# el cliente

# quien protege la infraestructura fisica en un data center
# AWS

# quien configura permisos IAM
# cliente

# quien mantiene el hardware fisico de los servidores
# AWS

# quien cifra los datos en s3
# Cliente

# quien aplica parches de seguridad al SO en ec2
# cliente

# quien es el responsable de la seguridad fisica del datacenter
# AWS

# quien configura security groups
# cliente

# quien administra el hipervisor
# AWS

# quien decide si un bucket s3 es publico o privado  ( contenedor donde se almacenan archivos en Amazon S3)
# cliente


# Truco mental rápido

- Si la pregunta habla de:

- Físico / infraestructura / datacenter → AWS

- Configuración / accesos / datos → Cliente **

* Seguridad de la nube
 # Esto incluye todo lo que corresponde a la infraestructura que AWS administra
  - Centros de datos físicos
  - Hardware
  - Redes
  - Servidores
  - Virtualización
  - Infraestructura Global
  - Servicios administrados (parte física y base del servicio)
  # AWS protege la infraestructura que hace funcionar la nube

 * Seguridad en la nube
 # Esto depende de como uses los servicios
  - Configuracion de IAM (usuarios y permisos)
  - Contraseñas y accesos
  - Configuracion de firewall(Security Groups)
  - Cifrado de datos
  - Sistemas operaticos(en EC2)
  - Aplicaciones instaladas
  - Parches del sistema operativo(Si usas EC2)  
  - Configuracion de bases de datos
  # Tú proteges lo que pones y configuras en la nube
  
