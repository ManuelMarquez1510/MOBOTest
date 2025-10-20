# Backend Python - Análisis de Entidades

Este proyecto contiene scripts en Python para el análisis y procesamiento de datos de entidades desde archivos CSV.

##  Descripción del Proyecto

El proyecto incluye dos scripts principales:

1. **`readCsv.py`**: Lee un archivo CSV con datos de entidades y genera un informe JSON con estadísticas
2. **`getListEntities.py`**: Función que devuelve las 3 entidades con las descripciones más largas

##  Requisitos

### Sistema

- Python 3.6 o superior
- pip (gestor de paquetes de Python)

### Dependencias de Python

- pandas >= 2.3.3
- pytest >= 8.4.2
- numpy >= 2.3.4

##  Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd backend-python
```

### 2. Crear entorno virtual (recomendado)

```bash
# En macOS/Linux
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requierements.txt
```

## Estructura de Archivos

```
backend-python/
├── README.md                    # Este archivo
├── requierements.txt            # Dependencias del proyecto
├── readCsv.py                  # Script para lectura de CSV y generacion de reportes
├── getListEntities.py          # Funcion para obtener entidades con descripciones más largas
├── test_getListEntities.py     # Tests unitarios para getListEntities
├── items.csv                   # Archivo CSV de ejemplo con datos de entidades
├── items_report.json           # Reporte generado (se crea automaticamente)
```

## Uso de los Scripts

### 1. readCsv.py - Generación de Reportes

Este script lee un archivo CSV y genera un informe JSON con estadísticas de las entidades

#### Funcionalidades:

- **Número total de entidades**: Cuenta todas las entidades en el archivo
- **Número de entidades activas**: Cuenta entidades con status = "activo"
- **Entidades con descripciones faltantes**: Identifica entidades sin descripción

#### Uso:

```bash
# Asegúrate de activar el entorno virtual primero
source venv/bin/activate

# Ejecutar el script (por defecto procesa items.csv)
python readCsv.py
```

#### Formato del CSV esperado:

El archivo CSV debe contener las siguientes columnas:

- `id`: Identificador único de la entidad
- `name`: Nombre de la entidad
- `description`: Descripción de la entidad (puede estar vacía)
- `status`: Estado de la entidad ("activo" o "inactivo")
- `created_at`: Fecha de creación

#### Salida:

- **Consola**: Imprime estadísticas básicas
- **Archivo JSON**: Genera `items_report.json` con el informe estructurado

#### Ejemplo de salida JSON:

```json
{
  "Numero de entidades": 7,
  "Numero de entidades activas": 5,
  "Numero de entidades sin descripcion": 2
}
```

### 2. getListEntities.py - Entidades con Descripciones Más Largas

Función que toma una lista de entidades y devuelve las 3 con las descripciones más largas.

#### Funcionalidades:

- Ordena entidades por longitud de descripción (de mayor a menor)
- Maneja valores `None` en descripciones
- Valida listas vacías y listas con menos de 3 elementos
- No modifica la lista original

#### Uso:

```bash
# Ejecutar el script directamente
python getListEntities.py

# O importar la función en otro script
from getListEntities import getListEntities
```

#### Parámetros:

- `entities` (list): Lista de diccionarios con entidades que deben contener al menos la clave "description"

#### Retorna:

- Lista con las 3 entidades que tienen las descripciones más largas

#### Manejo de errores:

- `ValueError("La lista esta vacía")`: Si se pasa una lista vacía
- `ValueError("La lista debe de contener a lo menos 3 elementos")`: Si la lista tiene menos de 3 elementos

## Testing

El proyecto incluye tests unitarios usando pytest.

### Ejecutar todos los tests:

```bash
# Activar entorno virtual
source venv/bin/activate

# Ejecutar tests
python -m pytest test_getListEntities.py -v
```

### Tests incluidos:

1. **`test_orderEntitiesTest`**: Verifica el orden correcto por longitud de descripción
2. **`test_noneValuesTest`**: Maneja valores None y verifica elementos nuevos
3. **`test_emptyListTest`**: Valida manejo de listas vacías
4. **`test_lessThanThreeElementsTest`**: Valida manejo de listas con menos de 3 elementos
5. **`test_noMutationTest`**: Verifica que la lista original no sea modificada

## Datos de Ejemplo

El archivo `items.csv` contiene datos de ejemplo con:

- 7 entidades en total
- 5 entidades activas
- 2 entidades sin descripción

## Validaciones

### readCsv.py:

- Valida que el archivo CSV exista
- Verifica que el archivo tenga extensión `.csv`
- Comprueba que contenga las columnas requeridas: `id`, `status`, `description`
- Valida que la ruta de salida sea un archivo `.json`

### getListEntities.py:

- Valida que la lista no esté vacía
- Verifica que contenga al menos 3 elementos
- Maneja descripciones nulas correctamente
