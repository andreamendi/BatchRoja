import pyrebase

config = {
	"apiKey": "AIzaSyDMBuXcG4LEjj71H-0vp6mn82SWdqk0cVc",
	"authDomain": "batchcroja17.firebaseapp.com",
	"databaseURL": "https://batchcroja17.firebaseio.com",
	"storageBucket": "batchcroja17.appspot.com",
}
#init firebase
firebase = pyrebase.initialize_app(config)

print(firebase)

#Create instance db
db = firebase.database()

#Create data
data = {"name":"Panchis","last_name":"Hernandez"}
data_4 = {"name":"Deni","last_name":"Olivares"}
db.child("users").child("user_123").set(data)
db.child("users").child("user_13").set(data_4)

#Get data
users = db.child("users").get()#Aquí me trae todo lo que tiene users, sí pongo .child("users_123")-> me trae especificamente el usuario 123
print(users.val())

#Update data
data_update = {"last_name": "Perez"}
update = db.child("users").child("user_123").update(data_update)
print(update)

all_users = db.child("users").get()
for user in all_users.each():
	print(user.key())
	print(user.val())
'''
def db_time(mensaje):
	print(mensaje["event"])
	print(mensaje["path"])
	print(mensaje["data"])

my_db = db.child("users").stream(db_time)#Escucha 
'''
#init storage
storage = firebase.storage()

#Upload image
storage.child("image/example.jpg").put("cat.jpg")

#Download
storage.child("image/example.jpg").download("gato.jpg") #Solita la descarga cuando la corres.

#URL
url = storage.child("image/example.jpg").get_url("1")
print(url)


