"""Configuracion centralizada del pipeline de datos climaticos."""

# Coordenadas de Villavicencio, Meta
LATITUDE = 4.14
LONGITUDE = -73.63
TIMEZONE = "America/Bogota"

# API Open-Meteo
API_URL = "https://api.open-meteo.com/v1/forecast"
API_PARAMS = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "daily": "temperature_2m_max,temperature_2m_min,rain_sum",
    "past_days": 30,
    "timezone": TIMEZONE,
}

# Base de datos MySQL (XAMPP)
DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "clima"
DB_TABLE = "datos_climaticos"
