"""TRANSFORM: Limpia y calcula metricas sobre los datos climaticos."""
import os
import json
import pandas as pd
import sys

# Agregar la raiz del proyecto al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

# Rutas relativas al directorio raiz del proyecto
ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
RAW_PATH = os.path.join(ROOT_DIR, "data", "raw", "clima.json")
PROCESSED_DIR = os.path.join(ROOT_DIR, "data", "processed")
OUTPUT_PATH = os.path.join(PROCESSED_DIR, "datos_limpio.csv")


def transform():
    """Lee clima.json, transforma y guarda en data/processed/datos_limpio.csv."""
    if not os.path.exists(RAW_PATH):
        print("[TRANSFORM] Error: no se encontro clima.json. Ejecuta extract.py primero.")
        sys.exit(1)

    os.makedirs(PROCESSED_DIR, exist_ok=True)

    with open(RAW_PATH, "r") as f:
        data = json.load(f)

    df = pd.DataFrame({
        "fecha": data["daily"]["time"],
        "temp_max": data["daily"]["temperature_2m_max"],
        "temp_min": data["daily"]["temperature_2m_min"],
        "lluvia_mm": data["daily"]["rain_sum"],
    })

    # Columna calculada
    df["rango_termico"] = df["temp_max"] - df["temp_min"]

    print(df.head())
    total_lluvia = df["lluvia_mm"].sum()
    print(f"[TRANSFORM] Total lluvia en {len(df)} dias: {total_lluvia} mm")

    df.to_csv(OUTPUT_PATH, index=False)
    print(f"[TRANSFORM] Datos guardados en {OUTPUT_PATH}")


if __name__ == "__main__":
    transform()
