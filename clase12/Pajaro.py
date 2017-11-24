from Animal import Animal

class Pajaro(Animal):
	
	def __init__(self,nombre,color,tipo,tamano):
		self.nombre = nombre
		self.color = color
		self.tipo = tipo
		self.tamano = tamano


	def pia(self):
		return "Pio Pio"


	def vuela(self):
		return "volando"

	
