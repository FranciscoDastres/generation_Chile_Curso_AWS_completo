* Que es
# es un servicio de pruebas que permite probar aplicaciones moviles y web en dispositivos reales hospedados por AWS 
# no son emuladores
# son dispositivos fisicos reales alojados por AWS
* Para que sirve
# Probar apps Android, IOS y web 
# Detectar errores según 
 * modelo del dispositivo
 * version del sistema operativo
 * tamaño de pantalla
# Automatizar pruebas sin mantener tu propio laboratorio de celulares

* Como funciona
 # subes tu app o url web
 # subes tus test o usas test predefinidos
 # AWS ejecuta las pruebas en multiples dispositivos reales
 # Obtienes
  * logs
  * capturas de pantalla
  * videos
  * reportes de errores 
* Todo on demand 
 # esto se refiere algo que se usa solo cuando lo necesitas, sin estar activo todo el tiempo

 * Cuando  usarlo
  # cuando tienes una app movil
  # necesitas probar muchos dispotivitos
  # quieres automatizar pruebas
  # no quieres comprar ni mantener telefonos fisicos

 * Cuando no usarlo
 # backend, apis, infraestructura, carga o pruebas de stresss
 # no reemplaza aws load testing , pruebas de backend pruebas unitarias servidor

 * se integra con
 # CI/CD
 # S3
 # IAM (permisos)
 # CloudWatch (log directos)
 
 # Frase para memorizar

 - Device Farm = pruebas de apps móviles en dispositivos reales en la nube