from compiler.sqlListener import sqlListener
from compiler.sqlParser import sqlParser

class CYDBMSListener(sqlListener):
    def __init__(self):
        pass
    
    def enterCreate_database_stmt(self, ctx:sqlParser.Create_database_stmtContext):
        print("Generando nueva base de datos")
        print(ctx.database_name().getText())
        
    def enterShow_databases_stmt(self, ctx:sqlParser.Show_databases_stmtContext):
        print("BITCONNNEEEECT")

    def enterUse_database_stmt(self, ctx:sqlParser.Use_database_stmtContext):
        print("cambiando a base de datos "+ctx.database_name().getText())

    def enterShow_tables_stmt(self, ctx:sqlParser.Show_tables_stmtContext):
        print("las tablas son estas...")

    def enterSelect_core(self, ctx:sqlParser.Select_coreContext):
        print("yes")
