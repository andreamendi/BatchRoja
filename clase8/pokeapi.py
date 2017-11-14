import requests

BASE_URL= "https://pokeapi.co/api/v2"
URI_POKEMON_1= "pokemon/1/"

URL= BASE_URL+URI_POKEMON_1

response = requests.get(URL)
print(response.json())
