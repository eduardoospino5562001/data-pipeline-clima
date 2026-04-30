# Pipeline ETL de Datos Climáticos (Villavicencio)

Un pipeline de datos (ETL) en Python que extrae, transforma y carga datos climáticos históricos de Villavicencio, Meta en una base de datos MySQL.

## Características
- **Extract:** Descarga automática de datos históricos desde la API pública de Open-Meteo (temperaturas y precipitaciones).
- **Transform:** Limpieza de datos y cálculo de métricas derivadas (rango térmico) usando **Pandas**.
- **Load:** Carga eficiente en MySQL con limpieza automática de datos duplicados.
- **Automatización:** Orquestación mediante script `.bat` para ejecución secuencial y configuración para ejecución diaria con el Programador de Tareas de Windows.

## Estructura del Proyecto
- `extract.py`: Script de extracción que consulta la API y guarda la respuesta cruda en `clima.json`.
- `transform.py`: Lee el JSON, transforma los datos a formato tabular (CSV) y calcula nuevas columnas.
- `load.py`: Lee el CSV procesado e inserta los registros en la base de datos MySQL.
- `pipeline.bat`: Archivo maestro que ejecuta los tres scripts en orden (Extract -> Transform -> Load).

## Requisitos
- Python 3.x instalado.
- MySQL corriendo (se recomienda **XAMPP** para entornos locales).
- Librerías de Python: `requests`, `pandas`, `pymysql`.

## Cómo ejecutar

1. **Instala las dependencias:**
   Abrir terminal y ejecutar:
   ```bash
   pip install requests pandas pymysql
   ```

2. **Iniciar base de datos:**
   Asegúrar de que el servicio de **MySQL** esté activo en el panel de XAMPP.

3. **Ejecuta el pipeline:**
   Hacer doble clic en `pipeline.bat` o ejecutar en la terminal:
   ```bash
   .\pipeline.bat
   ```

## Tecnologías utilizadas
- **Python** (Lenguaje principal)
- **Pandas** (Manipulación de datos)
- **MySQL** (Almacenamiento persistente)
- **Open-Meteo API** (Fuente de datos gratuita)

## Autor
Creado por Eduardo Ospino como proyecto de portafolio de Ingeniería de Datos.
