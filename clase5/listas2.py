#Uno
print("1")
lista = []
for i in range(0,100):
    lista.append(i)
print(lista)

print("________________________ \n")
print("2")
#dos
teclado = int(input("¿Qué número quieres multiplicar? \n"))

multi = []
for i in range(0,11):
    multi.append(i * teclado)
print(multi)

print("________________________ \n")

print("3")
#Tres
lista1=[4,76,3,12,65,3]
print(lista1)
lista2=[234,222,523,65]
print(lista2)
lista3=[]


lista3.extend(lista1)
lista3.extend(lista2)
print(lista3)

suma = 0
for i in lista3:
    suma += i
print("El resultado de tus listas es de: ", suma)
