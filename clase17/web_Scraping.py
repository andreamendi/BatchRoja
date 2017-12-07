#importar BeautifulSoup
from bs4 import BeautifulSoup

#modulo para hacer peticiones
import requests

#Link del sitio
URL = "http://www.gandhi.com.mx/adolescentes"

#obtener página web
page = requests.get(URL)

#Extrael el contenido con BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser') #<- lo que viene es un html y que haga un parceo

#Buscar en nuestra "soup" todos los elementos X
result_items = soup.find_all(class_='item')
#print(result_items)

#Itera en la lista que hicimos en el result_items
for item in result_items:
	name = item.find('a')['title']
	price = item.find(class_='price').text
	print(name)
	print(price)

