import requests
BASE_URL = "http://pokeapi.co/api/v2/"
num_pockemon  = input("Dame el número de el Pokemon que quieres saber su nombre")


def retorna_el_pockemon(num_pockemon):
    URL = BASE_URL + URI_POKEMON
    URI_POKEMON = "pokemon/" + num_pockemon
    response = requests.get(URL)
    diccionario = response.json()

    lista = diccionario['forms'][0]["name"]

    return (lista)

pokemon = retorna_el_pockemon(num_pockemon)
print(pokemon)
