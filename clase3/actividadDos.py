#!/usr/bin/python
#-*- coding: utf-8 -*-


#1
nUno = int(input("Escribe el primer número \n"))
nDos = int(input("Escribe el segundo número \n"))

resultado = nUno % nDos
if 0 == nUno % nDos:
    print ("Es entero")
else:
    print("No es entero ")
print("\n")

#2
print("Vamos con el segundo problema \n")
nTres = int(input("Escribe el primer número \n"))
nCuatro = int(input("Escribe el segundo número \n"))

if nTres > nCuatro:
    print("Tu número mayor es ",nTres)
else:
    print("Tu número mayor es ",nCuatro)
print("\n")

#3
print("Vamos con el tercer problema \n")

aUno = int(input("Escribe tu año actual \n"))
aDos = int(input("Escribe escribe otro año, en el pasado o en el futuro. \n"))

if aUno <= aDos:
    resultadoD =  aDos - aUno
    print("El tiempo entre tu año y el en el futuro es de: ", resultadoD)
elif aUno > aDos:
    resultadoT =  aUno - aDos
    print("El tiempo entre tu año y el antiguo es de: ", resultadoT)
else:
    print("Lo que ingresaste no es válido")

#4
print("Vamos con el Cuatro problema \n")
uno = int(input("Escribe el número 1 \n"))
dos = int(input("Escribe el número 2 \n"))
tres = int(input("Escribe el número 3 \n"))

if uno == dos == tres:
    print("Todos son iguales")
elif uno == dos != tres:
    print ("El número " + str(tres) + " es diferente")
elif tres== dos != uno:
    print ("El número " + str(uno) + " es diferente")
elif uno == tres != dos:
    print ("El número " + str(dos) + " es diferente")
elif uno != dos != tres:
    print ("Todos son diferentes " + str(uno) + " " + str(dos) + " " + str(tres))
else:
    print("Lo que ingresaste no es válido")


#5
print("Vamos con el Quinto problema \n")
uno5 = int(input("Escribe el número 1 \n"))
dos5 = int(input("Escribe el número 2 \n"))
tres5 = int(input("Escribe el número 3 \n"))

if uno5 == dos5 == tres5:
    print("Todos son iguales")
elif uno5 > dos5 and uno5 > tres5:
    print ("El número " + str(uno5) + " es mayor")
elif dos5 > uno5 and dos5 > tres5:
    print ("El número " + str(dos5) + " es mayor")
elif tres5 > uno5 and tres5 > dos5:
    print ("El número " + str(tres) + " es mayor")
elif uno5 == dos5:
    print ("Tus números más grandes son " + str(uno5) + " y " + str(dos5) + " es mayor")
elif uno5 == tres5:
    print ("Tus números más grandes son " + str(uno5) + " y " + str(tres5) + " es mayor")
elif tres5 == dos5:
    print ("Tus números más grandes son " + str(dos5) + " y " + str(tres5) + " es mayor")
else:
    print ("Lo que ingresaste no es válido")


#max(a,b,c)-> te da el máximo
