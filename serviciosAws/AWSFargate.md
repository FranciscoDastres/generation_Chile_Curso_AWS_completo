* Que es
# es un motor de computo serverless para contenedores ( capacidad de procesamiento de una maquina para ejecutar instrucciones y realizar calculos)
# ejecuta containers sin administrar servidores

* Sirve para
# Ejecutar contenedores Docker 

* Como funciona
# defines un contenedor
# ejecutas usando ECS + Fargate o EKS + Fargate
# AWS se encarga de 
 * servidores
 * escalado
 * disponibilidad
 * aislamiento

* tu manejas contendores. AWS maneja infraestructura

* Cuando usarlo
# quieres contenedores sin servidores
# Workloads 
 * microservicios
 * apis
 * jobs batch
# trafico variable
# menos operacion, mas foco en codigo

* ejemplo examen
# app basada en contenedores que deebe escalar automaticamente sin administrar Ec2