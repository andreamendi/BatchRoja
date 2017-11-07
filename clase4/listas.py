list1 = [2,3,4,5,6]
list2 = ["a","b","c",]
list3 = ["mate","minion", 1999,8987]
list4 = [list3,list2,list1]


print(list1)
print(list2)
print(list3)
print("________________________")
print(list4)


frutas = ["manzana","piña","sandia"]
print(frutas)

frutas.append("uva")
print("append")
print(frutas)

#frutas.extend(list2)
#print("extend")
#print(frutas)

frutas.insert(1,"fresa")
print("insert")
print(frutas)

frutas.pop(3) #En este caso el 3, vale la ubicación que va a eliminar
print("POP")
print(frutas)


frutas.remove("manzana") #Sí hay más de una, elimina la primera que se topa
print("REMOVE")
print(frutas)


frutas.reverse()
print("REVERSE")
print(frutas)


print("count")
print(frutas.count("piña"))

print("index")
print(frutas.index("piña"))
