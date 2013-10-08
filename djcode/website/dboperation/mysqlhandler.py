from django.db import connection

class MysqlDB(object):
	def __init__(self):
		pass

	def connection(self):
		self.cursor = connection.cursor()
	
	def execute(self, sqlstring):
		self.cursor.execute(sqlstring)
		
	def close(self):
		

