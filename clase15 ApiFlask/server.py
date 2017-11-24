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

	elif request.method == 'POST':
		return "Post"

if __name__ == '__main__':
	app.run(debug = True, port = 5000)