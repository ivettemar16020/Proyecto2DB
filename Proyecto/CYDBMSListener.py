from compiler.sqlListener import sqlListener
from compiler.sqlParser import sqlParser
from compiler.DatabaseManager import DatabaseManager as hello

class CYDBMSListener(sqlListener):
    def __init__(self):
        pass
    
    def enterCreate_database_stmt(self, ctx:sqlParser.Create_database_stmtContext):
        print("Generando nueva base de datos ")
        #print(ctx.database_name().getText())
        hello.createDatabase(self,ctx.database_name().getText())
        
    def enterShow_databases_stmt(self, ctx:sqlParser.Show_databases_stmtContext):
        #Query: SHOW DATABASES;
        print("Las bases de datos disponibles son: ")
        hello.getDatabases(self)

    def enterUse_database_stmt(self, ctx:sqlParser.Use_database_stmtContext):
        print("La base de datos a utilizar es: "+ctx.database_name().getText())

    def enterCreate_table_stmt(self, ctx:sqlParser.Create_table_stmtContext):
        #Query: create table hola(column1 hola);
        print("Creando tabla")
        print(ctx.table_name().getText())
        #hello.createTable(self, ctx.table_name().getText())

    def enterDrop_table_stmt(self, ctx:sqlParser.Drop_table_stmtContext):
        #Query: DROP TABLE table_name;
        print("Eliminando tabla")
        print(ctx.table_name().getText())

    def enterShow_tables_stmt(self, ctx:sqlParser.Show_tables_stmtContext):
        #Query: show tables;
        print("las tablas son estas...")
        hello.showTables(self, "hola")

    def enterSelect_core(self, ctx:sqlParser.Select_coreContext):
        #Query: Select * from table_name;
        print("Entro al select")
