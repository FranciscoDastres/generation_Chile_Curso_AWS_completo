# AWS WebServer – Notas Operativas

> 📌 **Orden:** lo más nuevo arriba (descendente)

---

## 🔥 Load Balancer (DNS)

**DNS del ELB:**

```
WebServerELB-1748297845.us-west-2.elb.amazonaws.com
```

**AMI asociada:**

```json
"ImageId": "ami-077c0d256555e3661"
```

---

## 🧱 AMI – Creación de plantilla

**Comando usado:**

```bash
aws ec2 create-image \
  --name WebServerAMI \
  --instance-id i-0c1ec5229b62c1bf2
```

---

## 🌐 DNS Público (EC2)

**URL de prueba:**

```
http://ec2-35-92-203-85.us-west-2.compute.amazonaws.com/index.php
```

**Public DNS Address:**

```
ec2-35-92-203-85.us-west-2.compute.amazonaws.com
```

**Obtener DNS vía AWS CLI:**

```bash
aws ec2 describe-instances \
  --instance-id i-0c1ec5229b62c1bf2 \
  --query 'Reservations[0].Instances[0].NetworkInterfaces[0].Association.PublicDnsName'
```

---

## 🆔 EC2 – Instance ID

```
i-0c1ec5229b62c1bf2
```

**Esperar a que la instancia esté corriendo:**

```bash
aws ec2 wait instance-running --instance-ids i-0c1ec5229b62c1bf2
```

---

## 🚀 Lanzamiento de nueva instancia EC2

```bash
aws ec2 run-instances \
  --key-name vockey \
  --instance-type t3.micro \
  --image-id ami-022bee044edfca8f1 \
  --user-data file:///home/ec2-user/UserData.txt \
  --security-group-ids sg-018a9c35f242877ef \
  --subnet-id subnet-069a0f9997b9f9b56 \
  --associate-public-ip-address \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=WebServer}]' \
  --output text \
  --query 'Instances[*].InstanceId'
```

---

## ⚙️ Configuración AWS CLI (⚠️ Sensible)

> ❗ **Las credenciales reales han sido omitidas por seguridad.**

```bash
mkdir -p ~/.aws && cat > ~/.aws/credentials << EOF
[default]
aws_access_key_id=REDACTED
aws_secret_access_key=REDACTED
aws_session_token=REDACTED
region = us-west-2
output = json
EOF
```

---

## 📋 Variables / Recursos Importantes

| Clave                     | Valor                      |
| ------------------------- | -------------------------- |
| **AMI ID**                | `ami-022bee044edfca8f1`    |
| **Security Group (HTTP)** | `sg-018a9c35f242877ef`     |
| **Command Host IP**       | `35.94.24.252`             |
| **Key Name**              | `vockey`                   |
| **Subnet ID**             | `subnet-069a0f9997b9f9b56` |

---

## 📝 Notas

* Región usada: **us-west-2**
* Instancia tipo: **t3.micro**
* Uso principal: **WebServer con ELB**
