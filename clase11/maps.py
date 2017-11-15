import requests
#Clave unica pro sólo mía de GOOGLE
#AIzaSyCG7YQwzFw1BFuFhAYCqhn3KJ3192E1L2Y


URL = "https://maps.googleapis.com/maps/api/directions/json?origin=Álvaro+Obregón+168+Roma+Norte,+MX&destination=Zócalo,+Plaza+de+la+Constitución,+MX+07073&key=AIzaSyCG7YQwzFw1BFuFhAYCqhn3KJ3192E1L2Y"

def mi_funcion():
    mapa = requests.get(URL)
    print(mapa.status_code)
    print(mapa.json())

mi_funcion()
