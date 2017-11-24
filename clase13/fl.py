from flask import Flask, jsonify
from flask import request

app = Flask(__name__) #este es un objeto tipo flask

@app.route('/') #el @ se llama decorador 
def index():
	return "Hola mundo"

@app.errorhandler(404)

@app.route('/params')
def params():
	parametro = request.args.get('params1','valor por default')
	parametro2 = request.args.get('params2','valor por default')
	return "El parametro es: {},{}".format(parametro,parametro2)

@app.route('/user/<name>/') #< int: name> para que pase los datos a enteros y no tengas que castear (o sea cambiar el formato)
def user(name):
	print(type(name))
	return "Los parametros por path son : {}".format(name)

if __name__ == '__main__': #esta es la manera de ejecutar flask
	app.run(debug = True, port = 5000) #reinicia cada que se hace un cambio, el puerto 5000 es el que se asigna por default (esta puesto solo para fines ilustrativos)