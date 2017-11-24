from flask import Flask, jsonify
from flask import request
import json
from triangulo import Triangulo
from rectangulo import Rectangulo

app = Flask(__name__)


'''
tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web', 
        'done': False
    }
]
'''
@app.errorhandler(404)
def page_not_found(e):
	return "ESTA PAGINA NO EXISTE"

@app.route('/area', methods = ['GET','POST'])
def index():
	if request.method == 'GET':
		 
		@app.route('/triangulo')
		def triangulo():
			base = int(request.args.get('base'))
			altura = int(request.args.get('altura'))
			triangulo= Triangulo(altura,base)
			areaTriangulo = triangulo.area()
			return jsonify({'area':areaTriangulo}) 


		@app.route('/rectangulo')
		def rectangulo():
			base = int(request.args.get('base'))
			altura =int(request.args.get('altura'))
			rectangulo = Rectangulo(altura,base)
			areaRectangulo = rectangulo.area()
			return jsonify({'area':areaRectangulo}) 

	elif request.method == 'POST':
		@app.route('/rectangulo')
		def rectangulo():
			body = request.json
			basej = body ['base']
			alturaj = body ['altura']
			rectangulo = Rectangulo(baseJ,alturaJ)
			areaRectangulo =rectangulo.area()
			return jsonify(dict(area=areaRectangulo))

		@app.route('/triangulo')
		def triangulo():
			body = request.json
			basej = body ['base']
			alturaj = body ['altura']
			rectangulo = Triangulo(baseJ,alturaJ)
			areaTriangulo =triangulo.area()
			return jsonify(dict(area=areaTriangulo))
		#jsonify castea algo que se parese a un JSON a un JSON

#http://127.0.0.1:5000/params?params1=HOLA
#http://localhost:5000/params?params1=Param_number_one&params2=Param_number_two




if __name__ == '__main__':
	app.run(debug = True, port = 5008)
