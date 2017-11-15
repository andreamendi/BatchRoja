import googlemaps
from datetime import datetime

now = datetime.now()
print(now)

origen = "Impact Hub, Roma Norte, Ciudad de México, CDMX"
destino = "Zócalo, Plaza de la Constitución, Centro, Ciudad de México, CDMX"

gmaps = googlemaps.Client(key="AIzaSyCG7YQwzFw1BFuFhAYCqhn3KJ3192E1L2Y")
direccion = gmaps.directions(origen, destino, mode = "driving", departure_time=now)
print(direccion)
