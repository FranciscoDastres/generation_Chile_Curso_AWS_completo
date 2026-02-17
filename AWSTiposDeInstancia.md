
# 1- Instancia dedicada
 # es el hardware fisico es exclusivo para ti
 - Características:
  # No compartes servidor físico con otros clientes
  # Cumple requisitos de licenciamiento (ej: software por núcleo físico)
  # Más cara
 - Cuándo usarla:
  # Requisitos regulatorios
  # Licencias que exigen hardware dedicado
  # Aislamiento fuerte

# 2- Instancia Bajo demanda (On-Demand)
  # Pagas por hora o segundo sin compromiso
  - Características
   # Sin contrato a largo plazo
   # Flexible
   # Más cara que reservada a largo plazo
  - Cuándo usarla:
   # Pruebas
   # Proyectos temporales
   # Cargas impredecibles

# 3- Instancia Spot
 # Usas capacidad sobrante de AWS con gran descuento
  - Caracteristicas
   # Hasta 90% más barata
   # AWS puede interrumpirla con aviso corto
   # No es estable para cargas críticas
  - Cuándo usarla:
  # Batch jobs
  # Procesamiento grande no crítico
  # HPC (Hight perfomance Computing = computación de alto rendimiento: sirve para ejecutar cargas de trabajo que requieren muchisima potencia de calculo)
  # Machine Learning

# 4- Instancia Reservada (Reserved Instance)
 # Te comprometes 1 o 3 años a cambio de descuento
  - Características
  # Mucho mas barata que On-Demand
  # Ideal para cargas estables
  # No cambia el tipo de máquina, cambia el modelo de facturación
  - Cuando usarla
  # Aplicaciones que siempre están encendidas
  # Bases de datos productivas
  # Backend permanente

* Tipo	        Precio	    Interrupción	Compromiso	    Uso ideal
# On-Demand	    Alto	    No	            No	            Temporal
# Spot	        Muy bajo	Sí	            No	            Batch/HPC
# Reservada	    Bajo	    No	            1-3 años	    Carga constante
# Dedicada	    Muy alto	No	            Opcional	    Licencias/regulación

# Necesita descuento y uso continuo → Reservada
# Muy barato pero puede apagarse → Spot
# Sin compromiso → On Demand
# Hardware exclusivo → Dedicada

# Uso corto + sin interrupciones → On demand