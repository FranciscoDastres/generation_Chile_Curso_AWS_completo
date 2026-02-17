* Que es?
 # Servicio de detección de amenazas (Threat detection)
 # Totalmente administrado
 # Analiza actividad sospechosa en tu cuenta AWS
 # Es un sistema de monitoreo inteligente de seguridad

* Para qué sirve?
 # Para detectar
  - Actvidad maliciosa
  - Credenciales comprometidas
  - Accesos inusuales
  - Instancias comprometidas
  - Comunicación con IPs maliciosas

* Ejemplos reales:
  # Un usuario IAM accede desde un país inusual
  # Una instancia EC2 se comunica con un servidor de comando y control
  # Intentos de minería de criptomonedas
  # Uso sospechoso de claves API

* Cómo funcion ?
 # GuardDuty analiza automáticamente
  - CloudTrail logs    
  - VPC Flow Logs
  - DNS Logs
 # Usa machine learning y feeds de inteligencia de amenzas
 # No necesitas instalar agentes

* Características importantes
 # Serverless
 # Activación con un clic
 # Genera "Findings"(Alertas) 
 # Integración com:
  # Security Hub 
  # EventBridge
  # Lambda

* Diferencia con otros servicios de seguridad
 # GuardDuty → Detecta amenazas
 # AWS Inspector → Escanea VUlnerabilidades
 # AWS Config → Evalúa configuraciones
 # Security Hub → Centraliza hallazgos
 # Shield → Protección contra DDoS

* GuardDuty = detección automática de amenazas en AWS 
# Necesitas detectar actividad maliciosa en tu cuenta AWS
# AmazonGuardDuty

# Necesitas evaluar si tus recursos cumplen reglas de configuración
# AWS Config

# Necesitas escanear vulnerabilidades en EC2
# AWS Inspector