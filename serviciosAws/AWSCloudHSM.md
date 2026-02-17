* Que es ? 
 # Servicio que proporciona Hardware Security Module (HSM) dedicado en la nube (dispositivo fisico especializado en criptografía que se usa para generar claves criptograficas, almacenar claves segura, firmar digitalmente , cifrar y descifrar datos)
 # Permite generar y almacenar claves criptográficas en hardware especializado
 # Tú tienes el control total de las claves
 # Es seguridad criptográfica a nivel hardware

* Para qué sirve?
 # Cumplir requisitos estrictos de compliance (cumplimiento de normas, leyes, regulaciones o políticas internas)
 # Manejar claves altamente sensibles
 # Firmas digitales
 # Encriptación avanzada
 # Aplicaciones financieras o gubernamentales

* Ejemplos reales:
 # Banco que necesita control total de claves
 # Firma digital de documentos legales
 # Infraestructura PKI empresarial
 # Sistemas que deben cumplir FIPS 140-2 Nivel 3 (estandar de seguridad del gobierno USA que define requisitos para modulos criptográficos, HW o software que realiza cifrado)

* Extra
 # FIPS → federal information processing standard

* Características importantes
 # HSM dedicado
 # Control total del cliente
 # Compatible con estándares criptográficos
 # Alta seguridad física y lógica  
 # Se integra con KMS si necesitas

* Diferencia con KMS 
 # AWS KMS → Servicio administrado y simple
 # CloudHSM → Control total más completo, más caro

* Si el examen dice: 
 # Máxima seguridad
 # Control total de claves
 # Requisitos regulatorios estrictos
 # Piensa en CloudHSM

* CloudHSM = control total de claves en hardware dedicado

 # Una empresa necesita control exlusivo de sus claves criptográficas
 # AWS CloudHSM

# Necesitas encriptación simple integrada con servicios AWS
 # AWS KMS

