* Que es ?
# un servicio serverless de consultas SQL
# permite analizar datos directamente en Amazon S3
# No necesitas servidores ni base de datos instalada
# solo pagas por los datos que escaneas!

* Para que sirve?
# Para consultar datos almacenados en : 
 - Archivos de S3
 - Logs
 - Datos en formato CSV
 - JSON
 - Parquet (formatop para almacenar datos  optimizado para analisis) guarda los datos por columnas
 - ORC ( tipo de dato como parquet)

* Ejemplos reales
# consultar datos de cloudtrail
# consultar logs de aplicaciones guardados en S3
# analizar datos exportados de una base de datos
# Crear reportes sin mover datos

* Como funciona
# los datos deben estar en S3
# Athena usa SQL estandar
# Se define un esquema usando AWS Glue Data Catalog
# Ejecuta consultas directamente  sobre los archivos
# No mueve los datos, los consulta donde están

* Ventajas clave
 - Serverless
 - No administra infraestructura
 - Escalable automáticamente
 - Ideal para análisis ad-hoc
 - Funciona muy bien con formatos optimizados como Parquet

* Frase para memorizar
# Athena = SQL directo sobre S3 sin servidores

* Preguntas tipo examen
# Tienes logs almacenados en S3 y necesitas analizarlos con SQL sin moverlos
*Amazon Athena*
# Necesitas hacer analisis puntual de datos en S3 sin crear una base de datos
*Amazon Athena*
# Necesitas un data wareshouse completo y persistente para BI
*Amazon Redshift*