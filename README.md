# API de Autos y Reservas

API REST desarrollada con **FastAPI** y **SQLModel** para la gestión de autos y reservas.

El proyecto implementa operaciones CRUD completas para dos entidades principales:

- **Autos**
- **Reservas**

Además, la aplicación fue diseñada con una arquitectura modular y está preparada para ser desplegada en **AWS EC2** utilizando **PM2** para mantener el servidor activo en segundo plano.

---

## Objetivo del proyecto

Desarrollar una API RESTful con FastAPI que permita:

- Registrar autos
- Consultar autos
- Actualizar autos
- Eliminar autos
- Crear reservas asociadas a un auto
- Consultar reservas
- Actualizar reservas
- Eliminar reservas

---

## Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal |
| FastAPI | Framework de la API |
| SQLModel | Modelado y acceso a datos |
| SQLite | Base de datos |
| Pydantic | Validación de datos |
| Uvicorn | Servidor ASGI |
| Git | Control de versiones |
| GitHub | Repositorio remoto |
| AWS EC2 | Despliegue de la API |
| PM2 | Ejecución de la API en segundo plano |

---

## Arquitectura del proyecto

```text
MI-PRIMER-EC2/
│
├── backend/
│   │
│   ├── src/
│   │   │
│   │   ├── crud/
│   │   │   ├── auto_crud.py
│   │   │   └── reserva_crud.py
│   │   │
│   │   ├── database/
│   │   │   └── database.py
│   │   │
│   │   ├── models/
│   │   │   ├── auto_model.py
│   │   │   └── reserva_model.py
│   │   │
│   │   ├── routers/
│   │   │   ├── auto_router.py
│   │   │   └── reserva_router.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── auto_schema.py
│   │   │   └── reserva_schema.py
│   │   │
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── venv/
│
├── .gitignore
└── README.md
```

---

## Organización de la arquitectura

| Carpeta | Función |
|---|---|
| `models` | Define las tablas SQLModel |
| `schemas` | Define los datos de entrada y salida |
| `crud` | Contiene las operaciones CRUD |
| `routers` | Define los endpoints de FastAPI |
| `database` | Configura SQLite y las sesiones |
| `main.py` | Inicializa FastAPI y conecta los routers |

El flujo de una petición es:

```text
Cliente
   ↓
Router
   ↓
CRUD
   ↓
SQLModel
   ↓
SQLite
```

---

# 🚘 Entidad Autos

Un auto contiene:

```text
id
marca
modelo
anio
placa
disponible
```

### Ejemplo

```json
{
  "marca": "Toyota",
  "modelo": "Corolla",
  "anio": 2024,
  "placa": "ABC-1234",
  "disponible": true
}
```

---

## Endpoints de Autos

| Método | Endpoint | Descripción |
|---|---|---|
| `POST` | `/autos/` | Crear un auto |
| `GET` | `/autos/` | Obtener todos los autos |
| `GET` | `/autos/{auto_id}` | Obtener un auto por ID |
| `PATCH` | `/autos/{auto_id}` | Actualizar un auto |
| `DELETE` | `/autos/{auto_id}` | Eliminar un auto |

---

# Entidad Reservas

Una reserva contiene:

```text
id
cliente
fecha_inicio
fecha_fin
auto_id
estado
```

Cada reserva está relacionada con un auto mediante:

```text
auto_id
```

### Ejemplo

```json
{
  "cliente": "Nicolas Rios",
  "fecha_inicio": "2026-09-20",
  "fecha_fin": "2026-09-25",
  "auto_id": 1,
  "estado": "confirmada"
}
```

---

## Endpoints de Reservas

| Método | Endpoint | Descripción |
|---|---|---|
| `POST` | `/reservas/` | Crear una reserva |
| `GET` | `/reservas/` | Obtener todas las reservas |
| `GET` | `/reservas/{reserva_id}` | Obtener una reserva por ID |
| `PATCH` | `/reservas/{reserva_id}` | Actualizar una reserva |
| `DELETE` | `/reservas/{reserva_id}` | Eliminar una reserva |

---

# Ejecución local

## 1. Clonar el repositorio

```bash
git clone https://github.com/cnrios1522/MI-PRIMER-EC2.git
```

Entrar al proyecto:

```bash
cd MI-PRIMER-EC2/backend
```

---

## 2. Crear entorno virtual

### Windows

```powershell
python -m venv venv
```

o:

```powershell
py -m venv venv
```

Activar:

```powershell
.\venv\Scripts\Activate.ps1
```

### Linux / Ubuntu

```bash
python3 -m venv venv
```

Activar:

```bash
source venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Entrar al código fuente

```bash
cd src
```

---

## 5. Ejecutar en modo desarrollo

```bash
fastapi dev
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```

Documentación Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# 📚 Documentación automática

FastAPI genera automáticamente una interfaz Swagger para probar todos los endpoints.

Disponible en:

```text
/docs
```

Desde ahí se pueden probar:

```text
POST
GET
PATCH
DELETE
```

sin necesidad de Postman.

---

# Base de datos

La aplicación utiliza **SQLite** como base de datos.

El archivo se crea automáticamente al iniciar la aplicación:

```text
autos_reservas.db
```

La conexión se configura en:

```text
src/database/database.py
```

Las tablas se crean automáticamente mediante:

```python
SQLModel.metadata.create_all(engine)
```

---

# Despliegue en AWS EC2

La API puede desplegarse en una instancia Ubuntu de AWS EC2.

## Actualizar Ubuntu

```bash
sudo apt update
sudo apt upgrade -y
```

---

## Instalar dependencias del sistema

```bash
sudo apt install git python3 python3-pip python3-venv -y
```

---

## Clonar el repositorio

```bash
git clone https://github.com/cnrios1522/MI-PRIMER-EC2.git
```

Entrar:

```bash
cd MI-PRIMER-EC2/backend
```

---

## Crear entorno virtual

```bash
python3 -m venv venv
```

Activar:

```bash
source venv/bin/activate
```

---

## Instalar requirements

```bash
pip install -r requirements.txt
```

---

## Entrar a `src`

```bash
cd src
```

---

## Ejecutar FastAPI

```bash
fastapi run
```

La API utilizará el puerto:

```text
8000
```

---

# Ejecución en segundo plano con PM2

Instalar Node.js:

```bash
sudo apt install nodejs -y
```

Instalar npm:

```bash
sudo apt install npm -y
```

Instalar PM2:

```bash
sudo npm install pm2@latest -g
```

Ejecutar FastAPI con PM2:

```bash
pm2 start ../venv/bin/fastapi --name fastapi-api --interpreter none -- run main.py --host 0.0.0.0 --port 8000
```

Comprobar:

```bash
pm2 list
```

Debe aparecer:

```text
fastapi-api    online
```

---

## Ver logs

```bash
pm2 logs fastapi-api
```

---

## Mantener la API activa después de reiniciar EC2

```bash
pm2 save
```

Luego:

```bash
pm2 startup
```

Ejecutar el comando generado por PM2 y finalmente:

```bash
pm2 save
```

---

# Acceso público

Después del despliegue en EC2:

```text
http://IP-PUBLICA:8000/
```

Swagger:

```text
http://IP-PUBLICA:8000/docs
```

---

# Funcionalidades implementadas

- CRUD completo de Autos
- CRUD completo de Reservas
- Relación entre Autos y Reservas
- Arquitectura modular
- Validación de datos
- SQLModel
- SQLite
- Documentación automática Swagger
- Control de versiones con Git
- Repositorio en GitHub
- Despliegue en AWS EC2
- Ejecución permanente mediante PM2

---

# Autor

**Nicolas Rios**

Proyecto desarrollado para la actividad:

**Autonomous Activity: FastAPI on EC2**

---

## Estado del proyecto

```text
FastAPI            ✅
SQLModel           ✅
SQLite              ✅
CRUD Autos          ✅
CRUD Reservas       ✅
Arquitectura modular ✅
Swagger             ✅
GitHub              ✅
AWS EC2             ✅
PM2                 ✅
```
