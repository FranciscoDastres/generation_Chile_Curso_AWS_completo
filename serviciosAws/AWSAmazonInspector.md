* Que es?
# servicio de evaluacion automatica de vulnerabilidades
# busca fallas de seguridad no ataques en vivo

* Para que sirve?
# Detectar vulnerabilidades
 * encontrar
  * CVEs ( common vulnerabilities and exposures , vulnerabilidades conocidas y publicas)
  * software desactualizado
  * configuraciones inseguras

 * evaluar
  * Ec2
  * Contenedores (ECR Elastic Container Registry, es donde guardas las imagenes docker) 
  * funciones Lambda

* Como funciona ?
 # Activas Inspector
 # Escanea recursos compatibles
 # Identifica vulerabilidades conocidas
 # Genera findings( es un hallazgo de seguridad: recurso afectado "imagen", "ECR", "Ec2","Lambda tiene tipo de severidad)
 # Envia resultados a Security Hub
 # es automatico y continuo

* Cuando usarlo
# quieres asber si tienes vulnerabilidades
# necesitas cumplir seguridad y compliance
# ejecutas EC2, containers o lambda  

* pregunta tipo examen
# Empresa requiere detectar vulnerabildiades en instancias Ec2