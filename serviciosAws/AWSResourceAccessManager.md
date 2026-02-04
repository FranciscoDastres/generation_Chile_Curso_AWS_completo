* Que es
# es un servicio que permite compartir recursos de AWS entre cuentas y dentro de una organizacion, compartir sin copiar ni duplicar

* Para que sirve 
# compartir recursos de forma segura
# evitar duplicacion de infraestructura
# centralizar administacion

* ejemplos de recursos que se comparten
# subnets
# VPC
# Route 53
# AWS Transit Gateway
# Licencias

* Como funciona
# flujo simple: cuenta A posee recurso 
# usa AWS ram para compartirlo
# cuenta B accede al recurso
# el recurso sigue siendo propiedad de la cuenta A
# Acceso compartido, no transferencia

* Cuando usarlo
# tienes multiples cuentas
# quieres una VPC central
# necesitas controlar costos y seguridad
# estas usando AWS organizations

* ejemplo de examen
# empresa con multiples cuentas quiere compartir una VPC sin duplicarla

* Frase para memorizar
# AWS RAM = comaprtir recursos entre cuentas sin duplicarlos
