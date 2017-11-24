from figura import Figura


class Triangulo(Figura):
	#(Animal) declara que es su papá, del que va a heredar
	
	def area(self):
		areaTri = ((self.base * self.altura)/2)
		return areaTri

