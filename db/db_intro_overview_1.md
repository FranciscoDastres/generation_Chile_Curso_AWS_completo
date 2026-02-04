# Datos y Bases de Datos

## ¿Qué son los datos?
### Los datos son partes y fragmentos de información sin procesar.
#### Las imágenes, palabras y números de teléfono son ejemplos de datos.

---

# ¿Qué es una base de datos?
## Una base de datos es un conjunto de datos que se organiza en archivos denominados **tablas**.
### Las tablas son una forma lógica de acceder a los datos, gestionarlos y actualizarlos.

### Tabla de muestra: Preferencia en mascotas

| Perros | Gatos | Caballos | Otro |
|--------|--------|----------|------|
| 17     | 122    | 7        | 4    |

---

# Profundización: modelos de datos y E.F. Codd

# Modelos de datos
## Los modelos de datos son **estructuras lógicas** de una base de datos.
## Los modelos de datos se utilizan para determinar cómo se pueden almacenar y organizar los datos.

---

# Modelo relacional de E.F. Codd
## El modelo relacional (RM) es un modelo de datos del Dr. Edgar F. Codd, matemático de IBM, desarrollado a finales de la década de 1960.
- Se desarrolló para mejorar la gestión de grandes cantidades de datos.
- Está basado en un dominio matemático llamado álgebra relacional.

---

# Modelo relacional

## Dos tipos de bases de datos

### 🟦 Relacionales
- Una **base de datos relacional** es un conjunto de elementos de datos que tienen relaciones predefinidas.
- Requiere una definición fija de la estructura de los datos.

### 🟧 No Relacionales
- Una **base de datos no relacional** es una base de datos que **no** sigue el modelo relacional.
- Las **bases de datos no relacionales no** requieren una definición fija de la estructura de los datos.

---

# 📊 Diferencias entre Bases de Datos Relacionales y No Relacionales

## 1. Modelo de Datos
### 🟦 Relacional (SQL)
- Basado en tablas (filas y columnas).
- Estructura rígida con schema definido.
- Relaciones mediante llaves primarias y foráneas.

### 🟧 No Relacional (NoSQL)
- No usa tablas tradicionales.
- Puede ser:
  - Documentos (JSON)
  - Clave-valor
  - Columnas
  - Grafos
- Estructura flexible o sin schema.

---

## 2. Escalabilidad
### 🟦 Relacional
- Escalabilidad vertical (más hardware).
- Limitado para escalar horizontalmente.

### 🟧 No Relacional
- Escalabilidad horizontal (agregar nodos).
- Ideal para sistemas distribuidos.

---

## 3. Consistencia vs Velocidad
### 🟦 Relacional
- Consistencia alta (ACID).
- Ideal para datos críticos.

### 🟧 No Relacional
- Enfoque BASE.
- Consistencia eventual.
- Más rápido en sistemas masivos.

---

## 4. Casos de Uso
### 🟦 Relacional
- ERP  
- Inventarios  
- Contabilidad  
- Reservas  

### 🟧 No Relacional
- Redes sociales  
- Apps de alto tráfico  
- Logs  
- Big Data  

---

## 5. Lenguaje de Consultas
### 🟦 Relacional
- Usa SQL.
- Permite JOIN y consultas complejas.

### 🟧 No Relacional
- Varía según el motor (MongoDB, Redis, Cassandra, Neo4j).

---

## 6. Ejemplos de Motores
### 🟦 Relacional
- MySQL  
- PostgreSQL  
- SQL Server  
- Oracle  

### 🟧 No Relacional
- MongoDB  
- Redis  
- Cassandra  
- Neo4j  

---

## ✔️ Resumen Comparativo

| Característica | Relacional (SQL) | No Relacional (NoSQL) |
|----------------|------------------|------------------------|
| Estructura | Tablas | Documentos / Columnas / Grafos / KV |
| Schema | Rígido | Flexible |
| Escalabilidad | Vertical | Horizontal |
| Consistencia | ACID | BASE |
| Rendimiento | Menor en volúmenes | Mayor en escalas grandes |
| Uso típico | Estructurado | Masivo / dinámico |

---

# Bases de datos relacionales

### Casos de uso:
- Comercio electrónico  
- CRM  
- Inteligencia empresarial  
- Análisis financiero  

### Bases de datos relacionales de ejemplo:
- MySQL  
- Amazon Aurora  
- PostgreSQL  
- Microsoft SQL Server  
- Oracle  

### Principales razones para utilizarlas:
- SQL compatible nativamente  
- Integridad de datos  
- Admite transacciones  

---

# DB No Relacional

## Casos de uso
- Detección de fraude  
- Internet de las cosas  
- Redes sociales  

## Bases NoSQL de ejemplo
- AWS DynamoDB  
- AWS Redshift  
- MongoDB  
- Apache HBase  

## Razones para utilizarlas
- Modelo flexible  
- Manejo de datos masivos  
- Escalan muy bien  

---

# Sistema de Gestión de Bases de Datos (DBMS)

## El DBMS es un software que proporciona funcionalidad de base de datos.

### Dos variantes:
- **Usuario único** → Microsoft Access  
- **Multiusuario** → Oracle, SQL Server, MySQL, IBM DB2  

---

# Ubicaciones

## En las instalaciones
- Los datos se almacenan en equipos y redes internas de la organización.

## En la nube
- Los datos se almacenan en centros de datos de proveedores como AWS.

---

# Base de Datos como Servicio (DBaaS)

### Características:
- Servidores alojados por un tercero.
- Reducción de costos.
- Administración completa (backups, parches, etc.)
- Muy rápido y escalable.

---

# Ejemplos de Interacción de Datos (DI)

## Interacción directa

### Analista de datos
- Escribe SQL directamente.
- Principalmente SELECT.

### Administrador de base de datos
- Usa todos los comandos SQL.

---

# Cliente - Servidor
- Usuarios: cliente, analista, administrador de BD.  
- Un servidor ejecuta la aplicación de base de datos.

---

# 🧩 Flujo entre aplicación, desarrollador y servidor de base de datos

## Equipo del desarrollador
- Usa Java + SQL.
- Incrusta SQL en la app.
- Publica la app.

## Usuario
- Usa la app desde su dispositivo.

## Aplicación cliente
- El usuario no escribe SQL.
- La app lo hace internamente.

## Servidor de base de datos
- Ejecuta SQL.
- Envía los resultados.

---

# 🏗️ Arquitectura de Aplicación Web de Tres Niveles

## 1. Nivel de Presentación
- Navegadores y móviles.
- Muestran contenido estático y dinámico.

## 2. Nivel de Aplicación
- Procesa la lógica del negocio.
- Genera contenido dinámico.

## 3. Nivel de Datos
- Almacena y gestiona la información.

---

# Tecnologías emergentes de almacenamiento
## Un banco de memoria en la nube
- Permite análisis, dashboards, big data, IA, aprendizaje automático.

---

# ¿Cuál es el propósito de un DBMS?
El DBMS administra, organiza, protege y permite acceder a los datos, de forma eficiente, segura y estructurada.

# Conceptos Clave de Bases de Datos

## 📘 Bases de Datos Relacionales (SQL)
Una **base de datos relacional** —también conocida como **base de datos SQL**— organiza la información en **tablas** formadas por filas y columnas.  
Este enfoque permite distribuir los datos en varias tablas relacionadas entre sí, reduciendo redundancia y mejorando la integridad de la información.

## 📙 Bases de Datos No Relacionales (NoSQL)
Una **base de datos no relacional** —o **NoSQL**— no utiliza el modelo tradicional basado en tablas.  
En su lugar, almacena los datos en **estructuras flexibles**, como documentos JSON, pares clave-valor, grafos o columnas, lo que permite una gran adaptabilidad a datos variados o no estructurados.

## 🖥️ Sistema de Gestión de Bases de Datos (DBMS)
Un **DBMS** (Database Management System) es el software encargado de proporcionar toda la funcionalidad necesaria para trabajar con bases de datos:  
almacenamiento, consultas, seguridad, respaldo, integridad de datos y administración general.

## 🔄 Formas de Interacción con Datos
Existen cuatro formas comunes en que los usuarios o aplicaciones interactúan con una base de datos:

1. **Interacción directa** – Comandos SQL ejecutados desde una consola o herramienta de gestión.  
2. **Cliente-servidor** – Un cliente envía consultas al servidor de base de datos mediante una interfaz.  
3. **Incrustación en código de aplicación** – El código de la aplicación contiene instrucciones SQL para manipular datos.  
4. **Aplicación de tres niveles** – Arquitectura web donde cliente, servidor de aplicación y servidor de base de datos trabajan en conjunto.

## 🏞️ Lago de Datos (Data Lake)
Un **lago de datos** funciona como un gran repositorio de información en la nube.  
Permite almacenar datos estructurados y no estructurados y ejecutar distintos tipos de análisis: paneles de control, visualizaciones, procesamiento de big data, análisis en tiempo real y modelos de aprendizaje automático.

