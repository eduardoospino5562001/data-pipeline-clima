import json
import pandas as pd

with open("clima.json", "r") as f:
    data = json.load(f)

df = pd.DataFrame({
        "fecha": data["daily"]["time"],
        "temp_max": data["daily"]["temperature_2m_max"],
        "temp_min": data["daily"]["temperature_2m_min"],
        "lluvia_mm": data["daily"]["rain_sum"]
    })

df["rango_termico"] = df["temp_max"] - df["temp_min"]

print(df.head())

total_lluvia = df["lluvia_mm"].sum()
print(f"Total lluvia en 37 dias: {total_lluvia} mm")
df.to_csv("datos_limpio.csv", index=False)