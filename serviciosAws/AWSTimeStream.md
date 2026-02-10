* Que es ?
# Una db serverless de series temporales ( time series)
# esta diseñada para datos que tienen tiempo como eje principal

* Para que sirven
# para guardar y consultar datos como 
 - metricas
 - sensores
 - iot
 - monitoreo
 - logs con tiemstamp
 - telemetria
# ejemplos reales
 - temperatura por minuto
 - cpu cada segundo
 - metricas de aplicaciones
 - datos de dispositivos IOT

* como funciona
 # cada registro tiene 
  - timestap
  - medidas(valores)
  - dimensiones(metadata)

* TimeStream separa datos en 
 # memory Store
  - datos recientes
  - muy rapido
  - para consultas en tiempo real

 # magnetic Store
  - datos historicos
  - mas barato
  - consultas menos frecuentes
 # AWS mueve los datos automaticamente  

 * Frase para memorizar
 # timestream = time-series, metricas,sensores,serverless

 * pregunta examen
 # necesitas almacenar metricas de sensores cada segundo y consultar promedios por hora y dia
  # amazon timeStream

 # una app tiene alta latencia pior muchas conusltas repetida a RDS se necesita una solucion en memoria
  # Amazon ElasticCache
  # Eñastoc Cache = cache en ram para acelerar apps