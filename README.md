# PacketScope

> PacketScope es una plataforma web para el descubrimiento de activos y evaluación básica de seguridad en redes locales.

El objetivo del proyecto es proporcionar una interfaz moderna que permita descubrir dispositivos en una red, identificar servicios expuestos, consultar vulnerabilidades conocidas (CVEs) y generar reportes de forma sencilla.

Este proyecto está desarrollado como parte de mi portafolio profesional para demostrar conocimientos en desarrollo backend, frontend, redes, Linux y ciberseguridad.

---

# Características

## Implementadas (v1)

- Autenticación mediante JWT
- Escaneo de hosts utilizando Nmap
- Descubrimiento de puertos abiertos
- Identificación de servicios y versiones
- Almacenamiento de resultados en PostgreSQL
- Historial de escaneos
- Dashboard web
- Documentación automática con Swagger
- Docker Compose

---

## Próximamente

- Consulta automática de CVEs
- Comparación entre escaneos
- Exportación de reportes PDF
- Programación automática de escaneos
- Dashboard con métricas
- Inventario de activos
- Agente remoto
- Alertas de cambios

---

# Tecnologías

## Backend

- Python
- FastAPI
- SQLAlchemy
- Alembic

## Frontend

- React
- Vite
- TailwindCSS

## Base de datos

- PostgreSQL

## Infraestructura

- Docker
- Docker Compose

## Herramientas

- Nmap
- Git
- GitHub Actions

---

# Arquitectura

```
                 Usuario

                    │

            Navegador Web

                    │

              React Frontend
                    │
        HTTP Requests (REST API)
                    │
             FastAPI Backend
                    │
     ┌──────────────┴──────────────┐
     │                             │
 PostgreSQL                  Nmap Scanner
     │                             │
     └──────────────┬──────────────┘
                    │
                Linux Host

```

---

# Capturas

*(Se agregarán cuando el proyecto esté más avanzado.)*

---

# Instalación

```bash
git clone ...

cd cyberinsight

docker compose up --build
```

---

# Roadmap

## Versión 0.1

- [x] Git
- [x] README
- [x] FastAPI
- [x] Docker
- [x] PostgreSQL (Docker)
- [x] SQLAlchemy (Engine + Session)
- [x] Probar conexión a la BD

- [x] Crear Base ORM
- [x] Modelo User
- [x] Instalar Alembic
- [x] Configurar Alembic
- [x] Primera migración
- [x] Crear tablas automáticamente


---

## Versión 0.2

- [ ] Login
- [ ] Autenticación JWT
- [ ] Usuarios

---

## Versión 0.3

- [ ] Ejecutar Nmap
- [ ] Obtener hosts
- [ ] Escaneo de puertos
- [ ] Inventario de hosts
- [ ] Guardar resultados

---

## Versión 0.4

- [ ] Dashboard
- [ ] Tabla de hosts
- [ ] Historial
- [ ] Reportes

---

## Versión 0.5

- [ ] Consulta de CVEs
- [ ] Exportación PDF

---

# Objetivos de aprendizaje

Este proyecto tiene como propósito reforzar conocimientos en:

- Arquitectura de software
- APIs REST
- Docker
- Linux
- PostgreSQL
- Redes
- Ciberseguridad
- Integración de herramientas externas
- Desarrollo Full Stack

---

# En desarrollo... [V0.1]

api/

Aquí vivirán los endpoints.

Ejemplo:

/users

/scans

/auth
models/

Aquí estarán las tablas de SQLAlchemy.

User

Scan

Host
schemas/

Aquí estarán los modelos de Pydantic.

Por ejemplo:

UserCreate

UserResponse

LoginRequest
services/

Aquí irá la lógica.

Por ejemplo:

Ejecutar Nmap

Consultar CVEs

Generar PDF
db/

Aquí vivirá todo lo relacionado con la base de datos.

Sesiones.

Conexión.

Engine.

core/

Aquí colocaremos cosas importantes para toda la aplicación.

Por ejemplo:

config.py

security.py

logging.py

# Licencia

MIT