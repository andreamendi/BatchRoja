import requests


class Respuestas():
	def saluda(self,sender_id):
		JSON = {"messaging_type": "RESPONSE",
				"recipient":{
				"id":sender_id
				},
				"message":{
				"text":"hello Mendi!"
					}
				}
		URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAACKGIMFaLEBANPX6XSS4Pvx8zWvF0ZAKc8JZBKsk5bMGKmAuLmt9rW6gQrubwjNKce5O0OiSvsO2nDdSvqNEnmrp2rdQ6UXJjfRDWv91HAOJBdII4lPER7sBr3uqieDgCX6ZCTCETL1gTKZB6QkZCdmJHdB23OLuI7mZBRxZCcCwZDZD'
		respuesta = requests.post(URL, json = JSON)
		return respuesta

	def quick(self,sender_id):
		JSON = {
		  "recipient":{
		    "id":sender_id
		  },
		  "message":{
		    "text": "Here's a quick reply!",
		    "quick_replies":[
		      {
		        "content_type":"text",
		        "title":"Search",
		        "payload":"POSTBACK_IMAGE",
		        "image_url":"https://www.anipedia.net/imagenes/caracteristicas-generales-de-los-gatos.jpg"
		      },
		      {
		        "content_type":"location"
		      },
		      {
		        "content_type":"text",
		        "title":"Something Else",
		        "payload":"POSTBACK_TEXT"
		      }
		    ]
		  }
		}
		
		URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAACKGIMFaLEBANPX6XSS4Pvx8zWvF0ZAKc8JZBKsk5bMGKmAuLmt9rW6gQrubwjNKce5O0OiSvsO2nDdSvqNEnmrp2rdQ6UXJjfRDWv91HAOJBdII4lPER7sBr3uqieDgCX6ZCTCETL1gTKZB6QkZCdmJHdB23OLuI7mZBRxZCcCwZDZD'
		send = requests.post(URL, json = JSON)
		return True

	def generic(self,sender_id):
		JSON = {
		  "recipient":{
		    "id":sender_id
		  },
		  "message":{
		    "attachment":{
		      "type":"template",
		      "payload":{
		        "template_type":"generic",
		        "elements":[

		        	{'title': 'Cotizar',
								  'image_url': "https://www.anipedia.net/imagenes/caracteristicas-generales-de-los-gatos.jpg",
								  'subtitle': 'Cotiza tu envío',
								  'buttons':[{'type': 'postback', 'title':'Quiero cotizar', 'payload': 220}]
								  },
								  {'title': 'Cotizar',
								  'image_url': "https://www.anipedia.net/imagenes/caracteristicas-generales-de-los-gatos.jpg",
								  'subtitle': 'Cotiza tu envío',
								  'buttons':[{'type': 'postback', 'title':'Quiero cotizar', 'payload': 220}]
								  }
		        ]
		      }
		    }
		  }
		}
		URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAACKGIMFaLEBANPX6XSS4Pvx8zWvF0ZAKc8JZBKsk5bMGKmAuLmt9rW6gQrubwjNKce5O0OiSvsO2nDdSvqNEnmrp2rdQ6UXJjfRDWv91HAOJBdII4lPER7sBr3uqieDgCX6ZCTCETL1gTKZB6QkZCdmJHdB23OLuI7mZBRxZCcCwZDZD'
		send = requests.post(URL,json = JSON)
		return True

	def pln(self,sender_id):
		JSON = { "messaging_type": "RESPONSE",
			"recipient":{
				"id":sender_id
			},
			"message":{
				"text": "¿Qué quieres?"
			}

		}
		URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAACKGIMFaLEBANPX6XSS4Pvx8zWvF0ZAKc8JZBKsk5bMGKmAuLmt9rW6gQrubwjNKce5O0OiSvsO2nDdSvqNEnmrp2rdQ6UXJjfRDWv91HAOJBdII4lPER7sBr3uqieDgCX6ZCTCETL1gTKZB6QkZCdmJHdB23OLuI7mZBRxZCcCwZDZD'
		send = requests.post(URL,json = JSON)
		return True