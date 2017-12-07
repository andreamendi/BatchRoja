import pyrebase
import random

class FirebaseUser():
	firebase = ""
	def __init__(self):
		config = {
			"apiKey": "AIzaSyDMBuXcG4LEjj71H-0vp6mn82SWdqk0cVc",
			"authDomain": "batchcroja17.firebaseapp.com",
			"databaseURL": "https://batchcroja17.firebaseio.com",
			"storageBucket": "batchcroja17.appspot.com"
		}
		
		firebase = pyrebase.initialize_app(config)
		self.firebase = firebase

	def createUser(self,data): #POST
		db = self.firebase.database()
		id_user = random.randint(52,100)
		db.child("users").child(id_user).set(data)
		return db.child("users").child(id_user).get().val()

	def getallusers(self): #GET
		db = self.firebase.database()
		return db.child("users").get().val()