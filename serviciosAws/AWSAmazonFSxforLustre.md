* Que es?
# servicio administrado de sistema de archivos de alto rendimiento
# Basado en Lustre(Linux + Cluster) (Un cluster es un grupo de máquinas (servidores) trabajando juntas como si fueran una sola.)
# Diseñado para la computacion de alto rendimiento (HPC)
# es un file system ultra rápido para cargas pesadas

* Para que sirve?
# Para workloads que necesitan:
 - Alto throughput (GB/s) (cantidad de datos que se pueden procesar o transferir por segundo)
 - Baja latencia
 - Procesamiento paralelo
 - Mucho acceso concurrente a archivos

# Ejemplos reales
 - Machine Learning
 - Renderizado de video
 - Simiulaciones cientificas
 - Genómica (Es el análisis del ADN completo de un organismo.)
 - Procesamiento masivo de datos
 - Analisis financiero de alta velocidad

* Como funciona
 # Se crea un sistema de archivos FSx for Lustre
 # Se monta en muntiples instancias EC2
 # Puede integrarse con S3

* Integracion con S3
 # Puede importar datos desde S3
 # Puede exportar resultados a S3
 # Ideal para pipelines de análisis (Un pipeline es una secuencia automática de pasos.)
 # Funciona muy bien con clusters (por ejemplo EC2 + GPU)

* Caracteristicas importantes
# Muy alto rendimiento
# Escala automaticamente
# Compatible con Linux
# Ideal para procesamiento paralelo
# Se paga por capacidad y throughput 

* Frase para memorizar 
# FSx for lustre 
* Que es lustre? 
# sistema de archivos distribuido de alto rendimiento (HPC)
# diseñado para 
 - procesar enormes volumenes de datos
 - entregar alto throughput ( cantidad de datos que se pueden procesar o transferir por segundo) 
 - trabajar con clusters de cientos o miles de servidores

# no es almacenamiento comun, es para cargas pesadas tecnicas

# pregunta examen 
 * necesitas procesar grandes volumenes de datos en paralelo con muy alto rendimiento
 # amazon FSx for lustre
 * tienes un workloead de machine learning que lee datos desde S3 y necesita alto throughput
 # Amazon Fsx for lustre
 * necesitas un file system compartido simple para varias EC2
 # Amazon EFS