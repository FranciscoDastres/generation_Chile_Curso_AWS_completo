* Que es?
# un servicio cache en memoria totalmente administrado
# diseñado especificamente para amazon dynamoDB
# reduce la latencia de milisegundos a microsegundos
# Es basicamente un ElasticCache pero solo para DynamoDB

* Para que sirve?
# Para acelerar lecturas frecuentes en DynamoDB como:
# Aplicaciones web de alto tráfico
# Juegos online
# Aplicaciones móviles
# Rankings en tiempo real
# Sistemas con muchas consultas repetidas

* Ejemplos Reales
# Tabla de usuarios consultada miles de veces por segundo
# Catalogo de productos muy consultado
# Leaderboards de videojuegos
# Perfiles de usuarios en apps móviles

* Comó funciona?
# Se coloca entre la aplicacion y DynamoDB
# La app consulta DAX en vez de ir directo a DynamoDB
# Si el dato está en cahé → responde de inmediato
# Si no está → lo obtiene de DynamoDB y lo guarda en caché
# Funciona a nivel de API ( no necesitas cambiar tus queries mucho)

* Caracteristicas importantes
# Totalmente administrado
# Altamente disponible(cluster)
# Compatible con API de DynamoDB
# Solo acelera lecturas (no esctritura directa en cache)
# reduce costos  de lectura en DynamoDB

* Diferencia con ElastiCache
# Dax → solo para Dynamo DB
# ElastiCache → para cualquier aplicación (Redis/Memcached)

# Frase para memorizar
*DAX = cache en ram para DynamoDB*

* Preguntas tipo examen
# Una aplicación usa DynamoDB y necesita microsegundos de latencia para lecturas frecuentes
*Amazon DAX*

* Necesitas acelerar consultas repetidas a RDS
# ElastiCache

* Necesitas una solución cache genérica para múltiples bases de datos
# ElastiCache