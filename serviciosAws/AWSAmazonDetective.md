* Que es ?
 # es un servicio de seguridad de AWS que permite investigar y analizar incidentes o actividades sospechosas en tu cuenta
  - Analiza datos de GuardDuty, CloudTrail y VPC Flow Logs
  - Usa Machine Learning interno para detectar patrones anómalos y relaciones sospechosas entre recursos y usuarios
  - No necesitas entrenar modelos; todo el análisis viene incorporado con el servicio

  # Detective encuentra la historia detrás de las alertas de seguridad
  # Convierte datos complejos en informacion visual y entendible
  # Usa ML para detectar comportamientos anómalos

* Para que sirve? 
 # Investigar incidentes de seguridad en AWS
 # Visualizar patrones anómalos y conexiones entre recursos
 # Reducir el tiempo para entender el alcance de un incidente
 # Integrarse con GuardDuty para análisis más profundos

* Ejemplos reales
 # Detectar acceso no autorizado a EC2 desde una IP desconocida
 # Investigar actividad sospechosa en IAM roles
 # Analizar tráfico anómalo en VPC Flow Logs
 # Ver relaciones entre cuentas y recursos tras un incidente de seguridad

* Como funciona ?
 # Recopila datos de GuardDuty, CloudTrail y VPC Flow Logs
 # Aplica machine learning para detectar patrones insuales
 # Modela relaciones entre usuarios, recursos y actividades
 # Permite investigar visualmente y encontrar la causa raíz de incidentes

* Características importantes
 # Integración automática con GuardDuty, CloudTrail y VPC Flow Logs   
 # Visualizacion gráfica de relaciones entre recursos y usuarios
 # Investigación rápida de incidentes
 # Detección de patrones anómalos en tiempo real
 # Servicio totalmente gestionado , sin infraestructura adicional

* Diferencias con otros servicios
 # GuardDuty: detecta amenazas y genera alertas; Detective investiga y visualiza las causas
 # Security Hub: Consolida alertas de múltiples servicios, pero no permite análisis detallado ni visualización de relaciones

# Detective usa machine larning para investigar y conectar los puntos de seguridad en AWS

 # ¿Cuál es el propósito principal de Amazon Detective?
 # Respuesta: b) Investigar y analizar incidentes de seguridad
 # 
 # ¿Qué servicios de AWS se integran automáticamente con Detective?
 # Respuesta: b) GuardDuty, CloudTrail, VPC Flow Logs
 # 
 # Diferencia principal entre GuardDuty y Detective:
 # Respuesta: a) GuardDuty alerta, Detective investiga y visualiza.

 # Amazon detective puede reemplazar compeltamente a Guardduty para detectar amenazas ?
  * NO, detective complementa, no reemplaza la detección de amenazas