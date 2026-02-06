* Que es?
# servicio hibrido que conecta tu infraestructura on premises con almacenamiento en AWS, haciendo que la nube se vea como storage local

* Para que sirve?
# extender storage local a la nube
# backups en AWS
# Archivos compartidos hibridos
# reemplazar cintas fisicas
# acceso local con respaldo en la nube

* Como funciona?
# despilegas un gateway on prem
# el gateway expone storage como
 - disco
 - fs
 - tape
# los datos 
 - se cachean localmente
 - se guardan en AWS(S3)

# AWS Storage gateway conecta aplicaciones on premise con almacenamiento en AWS de forma hibrida