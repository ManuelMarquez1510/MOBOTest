# API RESTful - CRUD

API desarrollada con Laravel para la gestión completa de entidades Items a través de operaciones CRUD.

## Descripción

Esta API permite realizar operaciones completas de gestión de items/entidades con los siguientes atributos:

-   **id**: Entero, auto-incremento, clave primaria
-   **nombre**: Cadena de texto
-   **descripción**: Texto (opcional)
-   **estado**: Enum ('activo', 'inactivo')
-   **fecha_creacion**: Timestamp

## Tecnologías

-   **Framework**: Laravel 12.x
-   **PHP**: ^8.2
-   **Base de datos**: SQLite
-   **Autenticación**: Laravel Sanctum

## Instalación

### Requisitos previos

-   PHP 8.2 o superior
-   Composer
-   SQLite

### Pasos de instalación

1. **Clona el repositorio**:

```bash
git clone <tu-repositorio>
cd backend
```

2. **Instala las dependencias**:

```bash
composer install
```

3. **Ejecuta las migraciones**:

```bash
php artisan migrate
```

4. **Inicia el servidor**:

```bash
php artisan serve
```

El servidor estará disponible en: `http://localhost:8000`

## Endpoints de la API

Base URL: `http://localhost:8000/api`

### 📖 Obtener todos los items

```http
GET /api/items
```

**Respuesta exitosa (200)**:

```json
{
    "message": "Items obtenidos correctamente",
    "status": "success",
    "code": 200,
    "data": [
        {
            "id": 1,
            "nombre": "Mi Item",
            "descripcion": "Descripción del item",
            "estado": "activo",
            "fecha_creacion": "2024-01-15T10:30:00.000000Z"
        }
    ]
}
```

**Si no hay items (200)**:

```json
{
    "message": "No se encontraron items",
    "status": "error",
    "code": 200
}
```

### Obtener item por ID

```http
GET /api/items/{id}
```

**Respuesta exitosa (200)**:

```json
{
    "message": "Item obtenido correctamente",
    "status": "success",
    "code": 200,
    "data": {
        "id": 1,
        "nombre": "Mi Item",
        "descripcion": "Descripción del item",
        "estado": "activo",
        "fecha_creacion": "2024-01-15T10:30:00.000000Z"
    }
}
```

**Item no encontrado (404)**:

```json
{
    "message": "No se encontró el item",
    "status": "error",
    "code": 404
}
```

### Crear nuevo item

```http
POST /api/items
Content-Type: application/json

{
    "nombre": "Nuevo Item",
    "descripcion": "Descripción opcional",
    "estado": "activo"
}
```

**Respuesta exitosa (201)**:

```json
{
    "message": "Item creado correctamente",
    "status": "success",
    "code": 201,
    "data": {
        "id": 2,
        "nombre": "Nuevo Item",
        "descripcion": "Descripción opcional",
        "estado": "activo",
        "fecha_creacion": "2024-01-15T11:00:00.000000Z"
    }
}
```

**Error de validación (400)**:

```json
{
    "message": "Error en la validacion de los datos",
    "status": "error",
    "code": 400,
    "errors": {
        "nombre": ["El campo nombre es obligatorio."],
        "estado": ["El estado seleccionado no es válido."]
    }
}
```

### Actualizar item

```http
PUT /api/items/{id}
Content-Type: application/json

{
    "nombre": "Item Actualizado",
    "descripcion": "Nueva descripción",
    "estado": "inactivo"
}
```

**Respuesta exitosa (200)**:

```json
{
    "message": "Item actualizado correctamente",
    "status": "success",
    "code": 200,
    "data": {
        "id": 1,
        "nombre": "Item Actualizado",
        "descripcion": "Nueva descripción",
        "estado": "inactivo",
        "fecha_creacion": "2024-01-15T10:30:00.000000Z"
    }
}
```

### Eliminar item

```http
DELETE /api/items/{id}
```

**Respuesta exitosa (200)**:

```json
{
    "message": "Item eliminado correctamente",
    "status": "success",
    "code": 200
}
```

## Estructura del Proyecto

```
backend/
├── app/
│   ├── Http/Controllers/Api/
│   │   └── itemController.php    # Controlador principal de la API
│   ├── Models/
│   │   └── Item.php             
│   └── ...
├── database/
│   ├── migrations/
│   │   └── 2025_10_20_110151_create_item_table.php
│   └── database.sqlite           # Base de datos SQLite
├── routes/
│   └── api.php                   # Rutas de la API
└── README.md
```

## Comandos útiles

```bash
# Ejecutar migraciones
php artisan migrate

# Limpiar cache
php artisan cache:clear

# Ver rutas disponibles
php artisan route:list

# Servidor de desarrollo
php artisan serve
```
