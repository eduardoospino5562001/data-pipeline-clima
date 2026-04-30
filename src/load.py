"""LOAD: Carga los datos transformados en MySQL."""
import os
import pandas as pd
import pymysql
import sys

# Agregar la raiz del proyecto al path para importar config
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from config.settings import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_TABLE

# Rutas relativas al directorio raiz del proyecto
ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
CSV_PATH = os.path.join(ROOT_DIR, "data", "processed", "datos_limpio.csv")


def load():
    """Lee datos_limpio.csv y los inserta en la tabla MySQL."""
    if not os.path.exists(CSV_PATH):
        print("[LOAD] Error: no se encontro datos_limpio.csv. Ejecuta transform.py primero.")
        sys.exit(1)

    df = pd.read_csv(CSV_PATH)

    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.execute(f"USE {DB_NAME}")

    cursor.execute(f"DELETE FROM {DB_TABLE}")

    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {DB_TABLE} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            fecha DATE,
            temp_max DECIMAL(5,1),
            temp_min DECIMAL(5,1),
            lluvia_mm DECIMAL(5,1),
            rango_termico DECIMAL(5,1)
        )
    """)

    for _, row in df.iterrows():
        cursor.execute(f"""
            INSERT INTO {DB_TABLE} (fecha, temp_max, temp_min, lluvia_mm, rango_termico)
            VALUES (%s, %s, %s, %s, %s)
        """, (row["fecha"], row["temp_max"], row["temp_min"], row["lluvia_mm"], row["rango_termico"]))

    conn.commit()
    print(f"[LOAD] Se insertaron {len(df)} registros exitosamente!")
    cursor.close()
    conn.close()


if __name__ == "__main__":
    load()
