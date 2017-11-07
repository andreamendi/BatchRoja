print("Palabras en una lista")
ListaIM =[]
valores=int(input("¿Cuántos valores vas a introducir en tu lista? "))
if valores <1:
    print("Imposible")
else:
    for i in range(0,valores):
        numeroL=str(input("Escribe la palabra "))
        ListaIM.append(numeroL)
    print(ListaIM)

    print("Tienes {}".format(len(ListaIM)))

palabra=str(input("¿Qué palabra quieres eliminar? "))
buscar=(ListaIM.index(palabra))
#ListaIM.remove(palabra) #Sí hay más de una, elimina la primera que se topa


for pala in ListaIM:
    print(pala)
    if pala == palabra:
        ListaIM.remove(palabra)

print(ListaIM)
