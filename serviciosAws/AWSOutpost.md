* Que es
# es un servicio que llega infraestructura de AWS fisicamente a tu datacenter on-premises

* Para que sirve
# Ejecutar servicios AWS localmente
# Mantener baja latencia cion sistemas on premise
# Cumplir requisitos regulatorios o legales
# Tener experiencia AWS Consistente(api consola.CLI)

* como funciona
# AWS instla racks de outpost en tu datacenter
# AWS gestiona el hardware
# usas servicios como 
 * Ec2
 * EBS
 * ECS / EKS
 * Todo se administra desde la misma consola de AWS

* cuando usarlo
# necesitas AWS + on-prem
# latencia baja(milisegundos)
# datos no pueden salir del datacenter
# aplicaciones legandy + cloud hibrido

* ejemplo tipo examen
# empresa financiera necesita ejecutar cargas AWS en su datacenter por cumplimiento normativo

* cuando no usarlo
# solo quieres conectarte a aws
# no necesitas latencia ultra baja
# no tienes datacenter propio
 * en esos casos
 #  VPC / Direct COnnect
 # Regiones AWS normales
 # Local Zones

* Outpost No es para ahorrar costos
* permite utilizar hardware instalado de aws en las instalaciones para ampliar y ejecutar servicios nativos de AWS disponibles en las instalaciones, si usa outpost, es posible ejecutar algunos servicios de AWS locamente mediante los mismos servicios, herramientas y las api de AWS

