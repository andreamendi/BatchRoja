#!/usr/bin/python
#-*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from sqlalchemy import text
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)#Es la que esta ligada a la Base de datos
print(db)

app.errorhandler(404)
def page_not_found(e):
	return "ESTA PAGINA NO EXISTE"

@app.route('/users', methods = ['GET','POST'])
def index():
	if request.method == 'GET':
		sql = text('select * from user_cinta')#La línea es esta <-
		result = db.engine.execute(sql)#Ve a la base de datos y ejecuta una línea, lo que esta en la L8
		names = []
		print(result)
		for row in result:
			names.append(row[1])
		return jsonify({"nombres":names})

	elif request.method == 'POST': #Estos son los datos que me va a dar en usuario en su body y yo los parceo en sus respectivas variables
	#Sí me mandan algo en el body que no tenga aquí declarado, se rompe y manda un 500, pero dice Raul que existen algoritmos
	#que hacen eso por default. 

		print(request.json)
		id_user=request.json['id']
		name = request.json['nombre']
		last_name = request.json['apellido']
		age = request.json['edad']

		sql = "insert into user_cinta(id_user,nombre,apellido,edad) values ({},'{}','{}',{});".format(id_user,name,last_name,age) 
				#La BD no acepta comillas dobles("), sólo comillas simples(')
				#Las que están en amarillo, son las que están en la BD
				#format, son las variables se concatenan una variable sin necesidad de poner un +
		result = db.engine.execute(sql)#Ejecuta el sql
		print(result)
		return jsonify({"msg":True}),201

		return "Post",201#sí está bbien, manda un 201, -> es que está creado

if __name__ == '__main__':
	app.run(debug = True, port = 5000)