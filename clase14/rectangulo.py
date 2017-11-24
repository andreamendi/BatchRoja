from figura import Figura


class Rectangulo(Figura):
	#(Animal) declara que es su papá, del que va a heredar
	def __init__(self,base,altura):
		super().__init__(base,altura)

	def area(self):
		areaRec = (self.base * self.altura)
		return areaRec
