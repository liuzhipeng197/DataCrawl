#encoding=utf-8
from users.models import User

def insert(user):
	u = User(username = user.username, password = user.password)
	u.save()

def editpassword(user):
	u = User.objects.get(pk = user.id)
	u.password = user.password
	u.save()

def isuserexist(user):
	if User.objects.filter(username = user.username, password = user.password):
		return "True"
	else:
		return "False"
	
