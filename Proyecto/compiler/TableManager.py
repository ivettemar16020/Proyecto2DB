import os

class TableManager:
	def createTable(self, name):
		print("something")

	def showTables(self, db_name):
        tables = os.listdir('../Bases/' + db_name + '/')
        print (tables)
