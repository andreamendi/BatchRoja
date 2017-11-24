from Animal import Animal

class Perro(Animal):
	#(Animal) declara que es su papá, del que va a heredar
	
	def __init__(self,nombre,color,raza,edad):
		self.nombre = nombre
		self.color = color
		self.raza = raza
		self.edad = edad

	def ladra(self):
		return "guagua"

	def mueve_cola(self):
		return "Muevete"

	


