# Proyecto Mobo Test - Caso Práctico

Este repositorio contiene la implementación completa de un caso práctico que abarca el desarrollo de diferentes componentes de software, incluyendo backend, frontend y análisis de datos.

## Estructura del Proyecto

El proyecto está organizado en las siguientes secciones principales:

```
mobo_test/
├── backend/           # API RESTful con Laravel
├── frontend/          # Aplicación React con Vite
├── backend-python/    # Scripts de análisis de datos con Python
└── README.md         # Este archivo principal
```

## Enlaces Rápidos

Cada sección tiene su propio README con información específica:

- **[Backend (Laravel)](./backend/README.md)** - API RESTful para gestión CRUD de entidades
- **[Frontend (React)](./frontend/README.md)** - Panel de control con interfaz de usuario
- **[Backend Python](./backend-python/README.md)** - Scripts de análisis de datos CSV

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd mobo_test
```

### 2. Navegación entre secciones

Para trabajar con cualquier parte del proyecto, puedes navegar a la carpeta correspondiente:

```bash
# Para el backend de Laravel
cd backend

# Para el frontend de React
cd frontend

# Para los scripts de Python
cd backend-python
```

## Descripción de cada Sección

### **Backend (PHP + Laravel)**

- **Tecnología**: Laravel 12.x con PHP 8.2+
- **Funcionalidad**: API RESTful completa con operaciones CRUD para gestión de entidades/items
- **Base de datos**: SQLite
- **Características**:
  - Validación de datos
  - Estructura de respuestas JSON estandarizada

### **Frontend (React)**

- **Tecnología**: React 18+ con Vite
- **Funcionalidad**: Panel de control con interfaz de usuario responsive
- **Características**:
  - Listado de elementos con filtros
  - Diseño responsive
  - Componentes modulares

### **Backend Python**

- **Tecnología**: Python 3.6+ con pandas y pytest
- **Funcionalidad**: Análisis y procesamiento de datos CSV
- **Scripts**:
  - `readCsv.py`: Análisis de archivos CSV y generación de reportes JSON
  - `getListEntities.py`: función en Python que toma una lista de entidades y devuelva las 3 entidades
con las descripciones más largas (ordenadas de mayor a menor).

## Requisitos del Sistema

### Para todo el proyecto:

- Git
- Sistema operativo compatible (Windows/macOS/Linux)

### Específicos por sección:

| Sección      | Requisitos                 |
| ------------ | -------------------------- |
| **Backend**  | PHP 8.2+, Composer, SQLite |
| **Frontend** | Node.js 18+, npm 9+        |
| **Python**   | Python 3.6+, pip           |
