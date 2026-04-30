import pandas as pd
import pymysql

df = pd.read_csv("datos_limpio.csv")
conn = pymysql.connect(host='127.0.0.1', user='root', password='')
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS clima")
cursor.execute("USE clima")
cursor.execute("DELETE FROM datos_climaticos")

cursor.execute("""
        CREATE TABLE IF NOT EXISTS datos_climaticos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            fecha DATE,
            temp_max DECIMAL(5,1),
            temp_min DECIMAL(5,1),
            lluvia_mm DECIMAL(5,1),
            rango_termico DECIMAL(5,1)
        )
    """)

for i, row in df.iterrows():
    cursor.execute("""
            INSERT INTO datos_climaticos (fecha, temp_max, temp_min, lluvia_mm, rango_termico)
            VALUES (%s, %s, %s, %s, %s)
        """, (row['fecha'], row['temp_max'], row['temp_min'], row['lluvia_mm'], row['rango_termico']))

conn.commit()
print(f"Se insertaron {len(df)} registros exitosamente!")
cursor.close()
conn.close()