print("Palabras en una lista")
ListaIM =[]
valores=int(input("¿Cuántos valores vas a introducir en tu lista?"))
if valores <1:
    print("Imposible")
else:
    for i in range(0,valores):
        numeroL=str(input("Escribe la palabra"))
        ListaIM.append(numeroL)
    print(ListaIM)
    print("Tienes {}".format(len(ListaIM)))

palabra=str(input("¿Qué palabra quieres buscar? "))
buscar=(ListaIM.count(palabra))

sustituir=str(input("¿Con qué palabras quiere sustitur?"))
listaIM[buscar]=sustituir
print(ListaIM)
