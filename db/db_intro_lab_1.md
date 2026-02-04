# Desafío DB 1 – Apuntes Mejorados

## 🟦 1. Acceder como superusuario

```bash
sudo su
cd /home/ec2-user/
```

## 🟦 2. Conectarse a MySQL

```bash
mysql -u root --password='re:St@rt!9'
```

---

# 🟩 Crear Base de Datos

```sql
CREATE DATABASE world;
```

### ✔️ Ver todas las bases de datos

```sql
SHOW DATABASES;
```

---

# 🟩 Crear Tabla `country`

```sql
CREATE TABLE world.country (
  `Code` CHAR(3) NOT NULL DEFAULT '',
  `Name` CHAR(52) NOT NULL DEFAULT '',
  `Conitinent` enum('Asia','Europe','North America','Africa','Oceania','Antarctica','South  America') NOT NULL DEFAULT 'Asia',
  `Region` CHAR(26) NOT NULL DEFAULT '',
  `SurfaceArea` FLOAT(10,2) NOT NULL DEFAULT '0.00',
  `IndepYear` SMALLINT(6) DEFAULT NULL,
  `Population` INT(11) NOT NULL DEFAULT '0',
  `LifeExpectancy` FLOAT(3,1) DEFAULT NULL,
  `GNP` FLOAT(10,2) DEFAULT NULL,
  `GNPOld` FLOAT(10,2) DEFAULT NULL,
  `LocalName` CHAR(45) NOT NULL DEFAULT '',
  `Government

```
