import requests
from bs4 import BeautifulSoup

def obtener_hashtags_tendencia():
    url = "https://tokboard.com/hashtags"
    response = requests.get(url)
    
    if response.status_code != 200:
        return "No se pudo acceder a los datos."

    soup = BeautifulSoup(response.text, 'html.parser')
    tabla = soup.find("table")
    filas = tabla.find_all("tr")[1:6]  # Tomar solo los 5 primeros hashtags

    hashtags = []
    for fila in filas:
        columnas = fila.find_all("td")
        if columnas and len(columnas) >= 2:
            hashtag = columnas[1].text.strip()
            hashtags.append(hashtag)

    return hashtags

# Ejecutar y mostrar
hashtags_tendencia = obtener_hashtags_tendencia()
print("🔺 Hashtags en tendencia:")
for i, tag in enumerate(hashtags_tendencia, start=1):
    print(f"{i}. {tag}")
