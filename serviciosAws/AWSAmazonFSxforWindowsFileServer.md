* Que es?
 # Servicio administrado de sistemas de archivos Windows
 # Compatible con SMB (Server MEssage Block)
 # Basado en windows server
 # Es como tener un File Server de Windows en AWS, sin administrarlo tú

* Para que sirve ?
 # Para Workloads que necesitan:
  - Compartir archivos en entorno Windows
  - Integracion con Active Directory 
  - Permisos NTFS
  - Aplicaciones Windows que requieren SMB

* Ejemplos Reales: 
 # Carpetas compartidas para empleados
 # Aplicaciones empresariales Windows
 # Servidores .NET que usan file shares
 # Home directories corporativos
 # Migraciones de File Server on-premise a AWS

* Como funciona? 
 # Se crea un sistema FSx for Windows
 # Se integra con Active Directory
 # Se monta en instancias EC2 Windows (o incluso on-premises vía VPN/Direct Connect)
 # Se accede mediante SMB
 # Soporta permitos NTFS y ACLs como un servidor Windows tradicional

* Características importantes
 # Totalmente administrado
 # Alta disponibilidad (Multi- AZ opcional) 
 # Backup automático
 # Compatible con Active Directory
 # Soporta deduplicación

* Diferencia con otros storage
 # EBS → Disco para una EC2
 # EFS → File system Linux (NFS)
 # FSx for Lustre → Alto rendimiento para HPC ( hight perfomance computing = computadora alto rendimiento)
 # FSx for Windows → File Server Windows (SMB + AD)
 # S3 → Objet Storage

* Frase para memorizar
 # FSx for Windows = File Server Windows administrado en AWS

* Una empresa quiere migrar su File Server Windows con permisos NTFS a AWS
 # Amazon FSx for Windows

* Una aplicacion Windows necesita almacenamiento compartido vía SMB
 # Amazon FSx for Windows

* Necesitas almacenamiento compartido para instancias Linux
 # Amazon EFS