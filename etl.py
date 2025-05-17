import requests
import datetime

def traducir_weathercode(codigo):
    codigos = {
        0: "Despejado",
        1: "Mayormente despejado",
        2: "Parcialmente nublado",
        3: "Nublado",
        45: "Niebla",
        48: "Niebla con escarcha",
        51: "Llovizna ligera",
        53: "Llovizna moderada",
        55: "Llovizna densa",
        56: "Llovizna helada ligera",
        57: "Llovizna helada intensa",
        61: "Lluvia ligera",
        63: "Lluvia moderada",
        65: "Lluvia intensa",
        66: "Lluvia helada ligera",
        67: "Lluvia helada intensa",
        71: "Nieve ligera",
        73: "Nieve moderada",
        75: "Nieve intensa",
        77: "Granizo",
        80: "Chubascos ligeros",
        81: "Chubascos moderados",
        82: "Chubascos intensos",
        85: "Chubascos de nieve ligeros",
        86: "Chubascos de nieve intensos",
        95: "Tormenta eléctrica",
        96: "Tormenta con granizo ligero",
        99: "Tormenta con granizo intenso"
    }
    return codigos.get(codigo, "Desconocido")

def extraer_datos_api():
    url = "https://api.open-meteo.com/v1/forecast?latitude=-41.56&longitude=-73.63&current_weather=true"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json().get("current_weather", {})
    # Agregar descripción y fecha extracción
    data["descripcion_clima"] = traducir_weathercode(data.get("weathercode", -1))
    data["extracted_at"] = datetime.datetime.now()
    return data
