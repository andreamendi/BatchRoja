class Auto:
#La clase no es un objeto, es con lo que se crea

#Aquí es *abstracto*, aún no exite. Ocupamos para definir. Pero no existe

	#Constructor 
	#Self, aquí, donde estoy parada, crea está variable "AQUÍ ES AQUÍ"
	def __init__(self,nombre_cons,color,motor):
		#Materia prima para crear un objeto
		#Siempre se va a ejecutar. Siempre y cuando este llamado.
		self.nombre = nombre_cons
		self.color = color
		self.ruedas = "4" #Esta es una constante
		self.motor = motor

	'''
	#Atributos, siempre lo van ha tener
	color = "ROJO"
	velocidad = "60"
	ruedas = "4"
	motor = "2.5"
	'''

	#Métodos, deben de estár cerrados para modificarlos.
	def arranca(self):
		print("Ruuuuuun el " + self.nombre)

	def frena(self):
		print("frena el " + self.nombre)

	def get_color(self): #Esta imprime el color, muestra.
		print(self.color)

	def set_color(self,new_color): #Aquí resetea el color.
		self.color = new_color


'''

Esto está comentado porque está siendo ejecutado en otro archivo. crearAuto.py

#Se ejecuta
#Una instancia que ya existe, cuando ponemos -nombre- = Auto() <- esto es que crear un objeto, pasarlo a la realidad. 
mustang = Auto('mustang','rojo','5.5')
mustang.arranca()
mustang.frena()
mustang.set_color("Azul")
mustang.get_color()


jetta = Auto('jetta','plata','2.5')
jetta.arranca()
jetta.frena()
jetta.get_color()

'''