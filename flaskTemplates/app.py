from flask import Flask, jsonify, render_template
from flask import request
import json

app = Flask(__name__)

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

@app.errorhandler(404) #Siempre un error 404
def page_not_found(e):
    #return redirect ('https://www.google.com.mx/')
	return render_template('index.html') #Esto redendera un html

@app.route('/tareas', methods = ['GET','POST']) #Petición Get y Post
def index():
	if request.method == 'GET':
		return jsonify({'tareas':tasks})
	elif request.method == 'POST':
		body = request.json


		return jsonify({
			'tareas':body['nombre'], 
			'Foo':body['edad']})

if __name__ == '__main__':
	app.run(debug = True, port = 5008)
