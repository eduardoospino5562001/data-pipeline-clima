import requests
import json

url = "https://api.open-meteo.com/v1/forecast"

params = {
     "latitude": 4.14,
     "longitude": -73.63,
     "daily": "temperature_2m_max,temperature_2m_min,rain_sum",
     "past_days": 30,
     "timezone": "America/Bogota"
}

response = requests.get(url, params=params)


if response.status_code == 200:
    data = response.json()
    print(f"Datos recibidos: {len(data['daily']['time'])} dias")
    print(f"Primeras fechas: {data['daily']['time'][:5]}")
    
    with open("clima.json", "w") as f:
        json.dump(data, f)
        print("Datos guardados en clima.json")
else:
    print(f"Error: codigo {response.status_code}")