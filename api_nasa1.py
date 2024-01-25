'''API: Application Programming Interface
NASA API: https://api.nasa.gov/
API_KEY_NASA: I8XzEPSyldHMqws5dlS2wOcLbcIXlRyHvmrrnwW3
Developer: Luis Daniel Rosero
Date: 24012024
Description: Get data from NASA API about comets
'''

import requests

def get_comet_data(api_key_nasa):
    print(":::: Comet Information ::::")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key_nasa}"

    try:
        #Realizar la solicitud a la API
        response = requests.get(url)
        response.raise_for_status() #Valida si se presenta algún error en la petición
        #Convertir la respuesta a formato JSON (JS Object Notation)
        datos = response.json()

        print(f"Comet name: {datos['name']}")
        print(f"Magnitude absolute: {datos['absolute_magnitude_h']}")
        print(f"Estimated diameter: {datos['estimated_diameter']['kilometers']['estimated_diameter_max']}")
        print(f"Estimated diameter: {datos['estimated_diameter']['feet']['estimated_diameter_max']}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición a la API de NASA: {e}")

api_key_nasa = 'I8XzEPSyldHMqws5dlS2wOcLbcIXlRyHvmrrnwW3'
get_comet_data(api_key_nasa)