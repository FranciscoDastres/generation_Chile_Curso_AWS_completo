* Que es ?
 # un servicio adminstrado para crear APis GraphQL
 # Permite sincronización de datos en tiempo real
 # Serverless y escalable automáticamente
 # Es una API inteligente basa en GraphQL

* Extra
 # Application Programming Interface = Mecanismo que permite que dos sistemas se comuniquen entre si
 # En desarrollo web 
  - El frontend envía una solicitud
  - El backend responde con datos
  - Normalmente usan HTTP
 
 # GraphQL → es Un lenguaje de consulta para APIs
  # fue creado por Meta (Antes Facebook)
  # A diferencia de API REST tradicional
  # el ciente decide exactamente qué datos quiere
  # No recibe información extra innecesaria
  # Todo pasa por un solo endpoint
  # Reduce Overfetching (reducir la cantidad de datos innecesarios que una API devuelve)
  * Ejemplo:
   # En rest si pides un usuario GET/usuario/1
    - El servidor te devuelve TODO el objeto
   # Tú especificas qué campos quieres:
    {
      usuario(id: 1) {
        nombre
        email
      }
    } 
* Para que sirve
  # Crear APis modernas para apps web y móviles
  # Sincronización en tiempo real
  # Backend para aplicaciones serverless
  # Manejar múltiples fuentes de datos con una sola API

 * Ejemplos reales:
  # App móvil que muestra datos actualizados en tiempo real
  # Chat en tiempo real
  # Dashboard que recibe actualizaciones automáticas
  # App que consulta DynamoDB y Lambda desde un solo endpoint
 
* Cómo funciona?
 # 1-Defines un schema GraphQL ( definicion estructural , que tipos de datos existen, que consultas, que mutaciones que campos tiene cada tipo)
 - ejemplo básico: 
  # type usuario {
     id: ID!
     nombre: String!
     email: String!
  }

  type Query {
    usuario(id: ID!): Usuario
  }
  
  * Extra 2 
     # Schema → Define estructura
     # Query  → Loo que el cliente pide
     # Resolver → La funcion que trae los datos reales
 # 2-Configuras resolvers (funcion que dice a GraphQL como obtener los datos que el cliente pidio)
# En AWS AppSync primero defines el schema, y luego conectas resolvers a bases de datos o Lambda.
# Una app móvil necesita datos en tiempo real, offline y consumir múltiples fuentes con una sola API.
 # 3- AppSync conecta el schema con:
  - DynamoDB
  - Lambda
  - RDS
  - OpenSearch
  - HTTP APIs
 # El cliente pide exactamente los datos que necesita 

# Necesitas una API GraphQL coin datos en tiempo real
# AWS AppSync

# Necesitas una API REST simple
# API Gateway

# Necesitas sincronizacion offline y tiempo real en una app móvil
# AWS AppSync