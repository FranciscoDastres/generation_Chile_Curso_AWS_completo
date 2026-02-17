* Qué es?
 # Un servicio de autenticación y autorización
 # Permite agregar login a aplicaciones web y móviles
 # Totalmente administrado y escalable
 # Maneja usuarios, registro, inicio de sesión y tokens

* Para qué sirve?
 # Registro de usuarios
 # Inicio de sesión (login)
 # Autenticación social (Google,Facebook,Apple)
 # Autenticación con proveedores empresariales (SAML)
 # Control de acceso a recursos AWS

* Ejemplos reales:
 # App móvil con login de usuario
 # Web con autenticación vía Google
 # API protegida con tokens JWT
 # Aplicación que necesita usuarios con permisos distintos

* Componentes principales
 # User Pools
 # Gestiona usuarios
 # Login y registro
 # Genera tokens JWT
 # Maneja contraseñas y MFA
 # Es el sistema de autenticación

* Como funciona?
 # 1 Usuario se registra o inicia sesion  
 # 2 Cognito Valida identidad
 # 3 Genera token JWT
 # 4 La app usa ese token para acceder a APis o recursos AWS

* Características importantes
 # Serverless
 # Soporta MFA
 # Escalable automáticamente
 # Integración con: 
  - API Gateway
  - Lambda
  - Amplify
  - ALB

* Diferencia con otros servicios
 # Cognito → Login y autenticación
 # IAM → Permisos para usuarios internos de AWS
 # AWS SOO / IAM identity Center → Acceso empresarial a cuentas AWS

* Cognito = Login y gestion de usuarioas para apps

* Necesitas agregar registro e inicio de sesión a una app móvil
# Amazon Cognito

* Necesitas dar acceso temporal a S3 después de login
# Cognito Identity Pool

* Necesitas administrar permisos para administradores AWS
# IAM