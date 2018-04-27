from compiler.sqlListener import sqlListener
from compiler.sqlParser import sqlParser
from compiler.DatabaseManager import DatabaseManager as hello

class CYDBMSListener(sqlListener):
    def __init__(self):
        pass
    
    #i) Crea una nueva base de datos y un nuevo directorio
    def enterCreate_database_stmt(self, ctx:sqlParser.Create_database_stmtContext):
        print("Generando nueva base de datos ")
        #print(ctx.database_name().getText())
        hello.createDatabase(self,ctx.database_name().getText())
    
    #ii) Cambia el nombre de una base de datos
    def enterAlter_database_stmt(self, ctx:sqlParser.Alter_database_stmtContext):
        #Query: ALTER DATABASE nombre RENAME TO nuevo;
        oldName =  ctx.database_name().getText()
        newName =  ctx.new_database_name().getText()
        print("¿Desea renombrar" + oldName + " y cambiarla por " + newName + "? (y/n)")
        respuesta = input()
        hello.alterDatabase(self, oldName, newName, respuesta)    
     
    #iii) Borra una base de datos
    def enterDrop_database_stmt(self, ctx:sqlParser.Drop_database_stmtContext):
        #Query: DROP DATABASE nombre; 
        print("La base de datos " + ctx.database_name().getText() + " ha sido eliminada")

    #iv) Muestra las bases de datos actuales 
    def enterShow_databases_stmt(self, ctx:sqlParser.Show_databases_stmtContext):
        #Query: SHOW DATABASES;
        print("Las bases de datos disponibles son: ")
        hello.getDatabases(self)

    #v) Selecciona la base de datos a trabajar 
    def enterUse_database_stmt(self, ctx:sqlParser.Use_database_stmtContext):
        print("La base de datos a utilizar es: "+ctx.database_name().getText())

   
   #vi) Crea una nueva tabla y un nuevo archivo 
    def enterCreate_table_stmt(self, ctx:sqlParser.Create_table_stmtContext):
        #Query: create table hola(column1 hola);
        print("Creando tabla")
        print(ctx.table_name().getText())
        #hello.createTable(self, ctx.table_name().getText())

    #vii)Cambia el nombre de una tabla 
    def enterAlter_table_stmt(self, ctx:sqlParser.Alter_table_stmtContext):
        print("La tabla " + ctx.table_name().getText() + " ha cambiado de nombre a " + ctx.new_table_name().getText())

    #viii) Alter table con una accion definida por el usuario 
    #Hmmmm
   
    #ix) Borra una tabla 
    def enterDrop_table_stmt(self, ctx:sqlParser.Drop_table_stmtContext):
        #Query: DROP TABLE table_name;
        print("Eliminando tabla")
        print(ctx.table_name().getText())

    #x) Muestra las tablas de la base de datos actual, si hay una en uso
    def enterShow_tables_stmt(self, ctx:sqlParser.Show_tables_stmtContext):
        #Query: show tables;
        print("las tablas son estas...")
        hello.showTables(self, "hola")

    #xi) Muestra la descripción de columnas de una tabla 
    #    en la base de datos incluyendo las restricciones
    def enterShow_columns_stmt(self, ctx:sqlParser.Show_columns_stmtContext):
        #Query: SHOW COLUMNS FROM nombre;
        print("Columnas")

    #SELECT 
    def enterSelect_core(self, ctx:sqlParser.Select_coreContext):
        #Query: Select * from table_name;
        print("Entro al select")
