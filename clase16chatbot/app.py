#!/usr/bin/python
#-*- coding: utf-8 -*-

from flask import Flask, request #Flask traer flask. Request traer el body
import requests
from respuestas import Respuestas


app = Flask(__name__)

ACCESS_TOKEN = 'EAACRQblPtUABAEPwWDET1FprP0zph7GQS5imejof9982CVOEszNpWb0N0z3lWNqtSe0NQpff18uZCVDBHEKfdNFrwCaMLEPoYK55Us6tu18ZAqxH7tOQEaHnGOavInH3ZCvgRoShyX6HyhaLv0fnO9c5R4xilpTZBEfvrG9EuQZDZD'
VERIFY_TOKEN = 'cintaroja'

@app.route('/')
def home():
	return 'Inicio del servidor'



@app.route('/webhook', methods = ['GET','POST'])
def webhook():
	if request.method == 'POST':
		mensaje = request.json
		print (mensaje)

		for event in mensaje['entry']:
			messaging = event['messaging']
			for event_message in messaging:
				sender_id = event_message['sender']['id']

				try:
					message = event_message['message']['text']
					pln = event_message['message']['nlp']['entities']['intent'][0]['value']
				
				except:
					message = "HOLA"
				
				print(message + ' por ' + sender_id + ' ' + str(pln))
				respuestas = Respuestas()

				if message.upper() == 'HOLA': 
					respuestas.saluda(sender_id)

				elif message.upper() == 'QUICK':
					respuestas.quick(sender_id)

				elif message.upper() == 'GENERIC':
					respuestas.generic(sender_id)

				elif pln.upper() == "QUIERO":
					respuestas.pln(sender_id)

		
		return 'ok'
		
	elif request.method == 'GET':
		if request.args.get('hub.verify_token') == VERIFY_TOKEN:
			return request.args.get('hub.challenge') #(args) -> Toma los parametros que vienen en el parametro GET
		return 'Verificar Token'






if __name__ == '__main__':
	app.run(port = 5000, debug = True)