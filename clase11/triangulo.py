from figura import Figura


class Triangulo(Figura):
	#(Animal) declara que es su papá, del que va a heredar
	
	def area(self,base,altura):
		areaTri = ((base * altura)/2)

