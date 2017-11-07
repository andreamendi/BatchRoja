print("Multiplo de dos")

for i in range(1,10001):
    print (i)
print("Listo")
print("________________________")

print("Multiplo de dos")
cuenta = 0
for i in range(1,1001):
    if i % 2 == 0:
        cuenta = cuenta +  1
        print (i)
print("________________________")


print("Elefante")
palabra = "ELEFANTE"
cuenta = 0
for i in palabra:
    if i == "E":
        cuenta += 1
        if cuenta == 3:
            print("La 3ª 'E'")


print("________________________")
#Cajero de OXXO


precio = 15
articulos = 6

if articulos >= 5:
    costo = articulos * precio
    total=costo * .95
    print("Aplica un descuento del 5% y el total es de $ ",total)

else:
    print("No aplica algún descuento")
