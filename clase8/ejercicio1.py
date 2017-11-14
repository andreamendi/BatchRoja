def tuplas_dic(lista_parametro):
	diccionario = {}
	lista_result = []
	for x,y in lista_parametro:
		diccionario[x] = lista_result
		lista_result.append(y)

	return diccionario

lista = [('BUENAS','TARDES'),('BUENAS','NOCHES'),('BUENOS','DIAS')]
print(tuplas_dic(lista))
