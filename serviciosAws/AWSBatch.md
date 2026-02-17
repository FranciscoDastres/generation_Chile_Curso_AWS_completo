* Que es ?
# servicio que ejecuta trabajos por lotes de forma automatica y escalabe sin que tu administres servidores
# tu defines que ejecutar
# AWS decide donde y con cuantos recursos

* para que sirve?
# para ejecutar procesos pesados, no interactivos como: 
 * procesamiento de datos 
 * analisis masivo
 * renderizado
 * machine learning batch
 * ETL (Extraer transformar Cargar)
 * Simulaciones
 * jobs que duran minutos u horas

* relacion con otros servicios
# batch + s3 → leer/ escribir datos
# batch + ECR → contenedores
# batch + IAM → permisos
# batch + cloudwatch → logs

* frase de certificacion
# aws batch ejecuta trabajos por lotes a gran escala, aprovisionando automaticamente la capacidad de computo necesaria y liberandola cuando finaliza la ejecucion

* pregunta
# una empresa necesita ejecutar trabajos de procesamiento que duran varias horas
# que servicio es el mas adecuado
# AWS BATCH