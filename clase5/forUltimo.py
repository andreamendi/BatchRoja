#!/usr/bin/python
#-*- coding: utf-8 -*-



valores =int(input("¿Cuántos números vas a darme?  \n"))
contador = 0
if valores < 1:
    print("Imposible")
else:
    pares = 0
    for i in range(1,valores+1):
        numero = int(input("Escribe el valor" + str(i) + " "))
        if numero % 2 == 0:
            pares += 1
    print ("Ha escrito " + str(pares) + " numeros pares y " + str(valores-pares) + " numeros inpares." )
