from figura import Figura


class Triangulo(Figura):
	#(Animal) declara que es su papá, del que va a heredar
	def __init__(self,base,altura):
		super().__init__(base,altura)

	def area(self):
		areaTri = ((self.base * self.altura)/2)
		return areaTri

