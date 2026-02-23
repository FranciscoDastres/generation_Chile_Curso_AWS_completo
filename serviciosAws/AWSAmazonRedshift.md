* Que es ?
 # es un data warehouse totalmente administrado en la nube  (Almacen de datos es un sistema especializado para almacenar grandes cantidades de datos integrados y oreanizados especialmente para analisis y toma de desciciones) centraliza datos de multiples fuentes, estandaraiza y limpia datos, permite analissi y reportes rapidos, incluso de grandes volumenes historicos de datos, soporta inteligencia de negocios cuadros de mando visualizaciones y mineria de datos

 * Diseñado para :
  # Analisis masivo de datos (OLAP Online analytical processing ( procesamiento analitico en  linea))
  # Consultas complejas sobre grandes volúmenes
  # Inteligencia de negocios
  # No es para aplicaciones transacionales
   - Que es OLAP
  # OLAP sirve para hacer consultas complejas rapido
  # Analizar datos historicos
  # Ver informacion desde diferentes dimensiones
  # Crear reportes dinamicos 

 * Para que sirve?
  # Para analizar terabytes o petabytes de datos rápidamente
  # Casos tipicos
   - Reportes empresariales
   - Dashboards de BI
   - Análisis financiero
   - Análisis de logs
   - Big Data analytics
   - Integración con herramientas como Power BI / Tableau 

 * Cómo funciona? 
  # Los datos se cargan en Redshift (Copy desde S3 es común)
  # Se almacenan en formato columnar
  # Se ejecutan consultas SQL optimizadas
  # Usa procesamiento paralelo masivo (MPP)

  # Arquitectura distribuida con nodos

  Arquitectura:
   - Leader node → coordina consultas
   - Compute nodes → procesan datos
   # Escala agregando nodos 

* Caracteristicas Claves
 # Almacenamiento columnar
 # Procesamiento paralelo
 # Comprension de datos
 # Escalable
 # Integracion con IAM
 # Alata velocidad para consultas analiticas
 # Integracion con S3

* Redshift Serverless
 # No necesitas administrar clústeres
 # Se ajusta automáticamente según carga  

 # Redshift vs RDS
 # Redshift	             RDS
 # Data warehouse	    Base de datos relacional
 # OLAP	                OLTP
 # Consultas complejas	Transacciones
 # PB de datos	        GB/TB
 # Análisis	            Aplicaciones


 # | Redshift                     | Athena                 |
 # | ---------------------------- | ---------------------- |
 # | Datos almacenados en cluster | Consulta directo en S3 |
 # | Alto rendimiento constante   | Serverless             |
 # | Ideal uso frecuente          | Ideal uso ocasional    |

# una empresa necesita analizar 500 TB de datos historicos para generar reportes complejos con SQL estandar
# Amazon Redshift

* Redshift = Data warehouse para analisis masivo con SQL