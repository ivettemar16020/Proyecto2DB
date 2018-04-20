from compiler.sqlListener import sqlListener
from compiler.sqlParser import sqlParser

class CYDBMSListener(sqlListener):
    def __init__(self):
        pass
    
    def enterCreate_database_stmt(self, ctx:sqlParser.Create_database_stmtContext):
        print("Generando nueva base de datos")
        print(ctx.database_name().getText())

"""
    def enterShow_databases_stmt():

    	for databaseName in databaseManager.getDatabases():
    		print(databaseName)
"""