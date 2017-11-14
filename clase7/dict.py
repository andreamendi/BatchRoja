#Reconoce que es una DICIONARIO porque esta entre {llaves}


diccionario = {"nombre": "Carlos", "edad": 22, "cursos":["Python", "flask"]}
print (diccionario)
print("El nombre es ",diccionario["nombre"])
print("Su edad ",diccionario["edad"])
print("Estudia ",diccionario["cursos"][0])#En la lista itera cuando le ponemos después del nombre de la llave, [0]

print("________________________")


for key,value in diccionario.items():
    print(key + " : " + str(value))

print("________________________")

nombre=input("¿Cuál es tu nombre? \n")
edad = int(input("¿Qué edad tienes? \n"))

dicc = {"nombre": nombre, "edad": edad, "cursos":["Python", "flask"], "Deporte": "natacion"}
print("El nombre es ",dicc["nombre"])
print("Su edad ",dicc["edad"])

print("________________________")

#Devuelve el número de elementos que tiene el diccionario.
print("La longitud es de: " + str(len(diccionario)))

#Devuelve una lista con las claves del diccionario
print(diccionario.keys())

#Devuelve una lista con los valores del diccionario
print(diccionario.values())

#Devulve el valor del elemento con su clave, y sí no lo encuentra devuelve un valor por default
print(diccionario.get("nore","Lilian"))


#Inserta un elemento al diccionario con su clave:valor, es como "append" en las listas
diccionario["key"] = "value"
print(diccionario)

#Borra la llave "Key"
diccionario.pop("key")
print(diccionario)

print("________________________")
print("Diccionario 2")
print("________________________")


#Devuelve la copia de un diccionario, o sea lo duplica.
diccionario2 = diccionario.copy()
print(diccionario2)

#Añade los elementos de una diccionario a otro, toma dos o más diccionarios en unos solo
diccionario.update(dicc)
print(diccionario)1
