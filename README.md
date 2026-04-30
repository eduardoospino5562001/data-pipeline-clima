# Pipeline ETL de Datos Climaticos - Villavicencio

Pipeline de datos que extrae informacion climatica de la API Open-Meteo, la transforma con Pandas y la carga en una base de datos MySQL.

## Caracteristicas

- **Extract:** Descarga 37 dias de datos (temperatura maxima/minima y lluvia) desde Open-Meteo API.
- **Transform:** Convierte JSON a DataFrame, calcula rango termico y metricas agregadas.
- **Load:** Carga datos limpios en MySQL con limpieza previa para evitar duplicados.
- **Configuracion centralizada:** Coordenadas, parametros de API y credenciales de BD en un solo archivo.

## Estructura del Proyecto

```
data-pipeline-clima/
├── src/                    # Scripts del pipeline
│   ├── extract.py          # Descarga datos de la API
│   ├── transform.py        # Limpieza y calculo de metricas
│   └── load.py             # Carga en MySQL
├── config/
│   └── settings.py         # Configuracion centralizada
├── data/                   # Datos (no se suben a Git)
│   ├── raw/                # clima.json (datos crudos)
│   └── processed/          # datos_limpio.csv (datos transformados)
├── pipeline.bat            # Orquestador secuencial
├── .gitignore
└── README.md
```

## Requisitos

- Python 3.10+
- MySQL (XAMPP recomendado)
- Librerias: `requests`, `pandas`, `pymysql`

```bash
pip install requests pandas pymysql
```

## Como Ejecutar

### Ejecucion individual

```bash
python src/extract.py     # Paso 1: Descargar datos
python src/transform.py   # Paso 2: Transformar datos
python src/load.py        # Paso 3: Cargar en MySQL
```

### Ejecucion automatica (todos los pasos)

```bash
pipeline.bat
```

## Automatizacion

Puedes programar la ejecucion diaria con el **Programador de Tareas de Windows**:
1. Abre "Task Scheduler" -> Create Basic Task
2. Trigger: Daily a las 6:00 AM
3. Action: Start a program -> selecciona tu `pipeline.bat`

## Configuracion

Edita `config/settings.py` para cambiar:
- Coordenadas (latitud/longitud)
- Parametros de la API
- Credenciales de la base de datos
