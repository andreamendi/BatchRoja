from Perro import Perro
from Pajaro import Pajaro

perrito = Perro("Fido", "Azul","OVNIE","3")
comiendo_perrito = perrito.comer()
ladra = perrito.ladra()
color_perrito = perrito.get_color()
nombre_perrito = perrito.get_nombre()
print(nombre_perrito)
print(color_perrito)
print(ladra)
print(comiendo_perrito)



pajarito = Pajaro("Pia","Rojo","MARCIANO","Mediano")
comiendo_pajarito = pajarito.comer()
pia = pajarito.pia()
color_pajarito = pajarito.get_color()
nombre_pajarito = pajarito.get_nombre()
print(nombre_pajarito)
print(color_pajarito)
print(pia)
print(comiendo_pajarito)
print()


#liskov substitution
def jauria (Animal):
	return Animal.comer()

print(jauria(perrito))