from figura import Figura


class Rectangulo(Figura):
	#(Animal) declara que es su papá, del que va a heredar
	
	def area(self):
		areaRec = (self.base * self.altura)
		return areaRec
