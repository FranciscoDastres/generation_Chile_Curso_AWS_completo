* Que es 
# es un servicio de almacenamiento de objetos altamente escalable, duradero y disponible en AWS
# guarda datos como
 * archivos
 * imagenes
 * videos
 * backups
 * logs
 * datos estaticos

* para que sirve
# almacenar datos de forma segura y duradera
# backups y recuperacion
# hosting de contenido estatico
# data lakes (Un Data Lake es un repositorio central donde guardas grandes cantidades de datos en bruto, tal como vienen, sin procesar)
# almacenamiento para otras apps AWS

* como funciona 
# los datos seguardan como objetos
# los objetos viven dentro de buckets
# cada objeto tiene
 * datos
 * metadata (es dato sobre un dato, info que describe el dato ej imagen : tamaño fecha resolucion etc)
 * una key (nombre)

* clases de almacenamiento
# S3 standar = acceso frecuente
# S3 intelligent tiering = acceso impredecible
# S3 standar-IA = poco acceso
# S3 One Zone IA = poco acceso 1 AZ
# S3 glacier instant retrieval = acceso rapido
# S3 glacier flexible retrieval = archivo
# S3 Glacier Deep Archive = Archivo muy largo plazo

*** mas barato = mas lento de recuperar ***

* pregunta examen
# una empresa necesita almacenar imagenes y videos con alta durabilidad y acceso global . amazon s3
# datos que se acceden una vez al año y deben ser lo mas barato posible . s3 glacier deep archive
# empresa quiere alojar sitio web estatico con bajo costo. amazon s3

* pregunta trampa 
# una app necesita montar un sistema de archivos compartido entre varias instancias EC2
# EFS (elastic file sistem, sistema de archivos que se puede montar simultaniamente en multiples instancias ec2)
