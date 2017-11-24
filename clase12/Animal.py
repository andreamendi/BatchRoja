class Animal:

	def __init__(self,color,nombre):
		self.color = color
		self.nombre = nombre

#Una función para cada cosa

	def comer(self):
		return "Come"

	def get_color(self):
		return self.color

	def get_nombre(self):
		return self.nombre
