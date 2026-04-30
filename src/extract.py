"""EXTRACT: Descarga datos climaticos de la API Open-Meteo."""
import os
import json
import requests
import sys

# Agregar la raiz del proyecto al path para importar config
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from config.settings import API_URL, API_PARAMS

# Rutas relativas al directorio raiz del proyecto
ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
RAW_DIR = os.path.join(ROOT_DIR, "data", "raw")
OUTPUT_PATH = os.path.join(RAW_DIR, "clima.json")


def extract():
    """Descarga datos de la API y los guarda en data/raw/clima.json."""
    os.makedirs(RAW_DIR, exist_ok=True)

    response = requests.get(API_URL, params=API_PARAMS)

    if response.status_code == 200:
        data = response.json()
        dias = len(data["daily"]["time"])
        print(f"[EXTRACT] Datos recibidos: {dias} dias")
        print(f"[EXTRACT] Primeras fechas: {data['daily']['time'][:5]}")

        with open(OUTPUT_PATH, "w") as f:
            json.dump(data, f)
        print(f"[EXTRACT] Datos guardados en {OUTPUT_PATH}")
    else:
        print(f"[EXTRACT] Error: codigo {response.status_code}")
        sys.exit(1)


if __name__ == "__main__":
    extract()
