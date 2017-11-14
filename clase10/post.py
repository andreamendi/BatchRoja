import requests
URL_BASE = "https://goodreads-devf-aaron.herokuapp.com"

def mi_peticion_post(email, password):
    URI = "/api/v1/users/"
    URL = URL_BASE + URI

    json_send = {
        "email": email,
        "password": password,
    }
    response = requests.post(URL,json = json_send)
    return response

respuesta = mi_peticion_post("andreamendi","HolaPyhton")
print(respuesta.status_code)
print(respuesta.json())
