def mi_funcion():
    #Todo el bloque de código que se ejecuta cuando se llame a la función
    print("Hola soy una función")

mi_funcion()


#Parametros y parametro con un valor por dafault
def suma_de_dos_mas_dos(num1, num2, num4=None):
    #num1 y num2 son parametros
    suma = num1 + num2
    print
    print(num4)
    print(str(suma))

suma_de_dos_mas_dos(3,4,7) #num1 toma a 3, num2 toma a 4, y así. Siempre hay que llamar a la función

def funcion_return(num1, num2):
    suma = num1 + num2
    return suma

def funcion_mult(num1, num2, num3):
    if num1 ==2:
        return "Numero 2"
    else:
        return num3
sumar = funcion_return(2,2)
#Todo lo que ejecuta y escupe un resultado, lo escupe como un valor y hay que guardarlo en una variable.

multiple = funcion_mult(3,2,999)
print(multiple)
