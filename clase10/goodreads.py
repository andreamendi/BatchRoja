import requests

BASE_URL = "https://goodreads-devf-aaron.herokuapp.com"
URI_GOODREADS = "/api/v1/authors/"
print('holi')

def retorna_la_biografia():
    URL = BASE_URL + URI_GOODREADS
    response = requests.get(URL)
    print('holi')
    lista_diccionario = response.json()
    for i in lista_diccionario:
        print(i["biography"])

'''
    for i in range(len(lista_diccionario)):

        nombre = lista_diccionario[i]["name"]
        apellido = lista_diccionario[i]["last_name"]
        biografia = lista_diccionario[i]["biography"]

        voy_a_retornar = nombre + apellido + biografia
        #print(voy_a_returnar)
'''

retorna = retorna_la_biografia()
print(retorna)

'''
retorna = retorna_la_biografia()
print(retorna)
'''
