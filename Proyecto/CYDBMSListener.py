from compiler.sqlListener import sqlListener
from compiler.sqlParser import sqlParser
from compiler.DatabaseManager import DatabaseManager as hello
import os
import json

class CYDBMSListener(sqlListener):
    def __init__(self):
        pass

    #i) Crea una nueva base de datos y un nuevo directorio
    def enterCreate_database_stmt(self, ctx:sqlParser.Create_database_stmtContext):
        #print("Generando nueva base de datos ")
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
    #FALTA: “¿Borrar base de datos nombre_BD con N registros? (si/no)” Donde N es la sumatoria de los registros de todas las tablas en la base de datos.
    def enterDrop_database_stmt(self, ctx:sqlParser.Drop_database_stmtContext):
        #Query: DROP DATABASE nombre; 
        dbName = ctx.database_name().getText()
        print("¿Está seguro que desea borrar la tabla " + dbName+ "? (y/n)")
        respuesta = input()
        hello.dropDatabase(self, dbName, respuesta)

    #iv) Muestra las bases de datos actuales 
    def enterShow_databases_stmt(self, ctx:sqlParser.Show_databases_stmtContext):
        #Query: SHOW DATABASES;
        hello.getDatabases(self)

    #v) Selecciona la base de datos a trabajar 
    def enterUse_database_stmt(self, ctx:sqlParser.Use_database_stmtContext):
        #Query: USE DATABASE name; 
        name = ctx.database_name().getText()
        hello.useDatabase(self, name)

   
   #vi) Crea una nueva tabla y un nuevo archivo 
    def enterCreate_table_stmt(self, ctx:sqlParser.Create_table_stmtContext):
        #Query: create table hola(column1 hola);
        #Query con constraint: create table people (ID int, constraint PRIMARY KEY(ID));
        #Query 2 constraints: create table People(ID int, Name String, CONSTRAINT PK_Person PRIMARY KEY (ID), CONSTRAINT PAL FOREIGN KEY (Name) REFERENCES Potato(Name))
        #print(ctx.table_name().getText())
        hello.createTable(self, ctx.table_name().getText(), ctx.column_def())
        constraint_list = ctx.table_constraint()
        for i in range(len(constraint_list)):
            print(constraint_list[i].getText())

    #vii)Cambia el nombre de una tabla 
    def enterAlter_table_stmt(self, ctx:sqlParser.Alter_table_stmtContext):
        #print("La tabla " + ctx.table_name().getText() + " ha cambiado de nombre a " + ctx.new_table_name().getText())
        oldName = ctx.table_name().getText()

        #viii) Alter table con una accion definida por el usuario 
        specificStmt = ctx.alter_table_specific_stmt()
        #print(specificStmt)

        #isinstance(object,type)
        if (isinstance(specificStmt, sqlParser.AlterRenameToContext)):
            #Cuando el query es: "alter table name rename to new_name"
            newName = specificStmt.new_table_name().getText()
            hello.alterTabName(self, oldName, newName)
        
        elif (isinstance(specificStmt, sqlParser.AlterAddColumnContext)):
            #Query: ALTER TABLE table_name ADD COLUMN nombre_columna tipo 
            column_name = specificStmt.column_def().column_name().getText()
            column_type = specificStmt.column_def().type_name().getText()
            hello.addColumn(self, oldName, column_name, column_type)

        elif (isinstance(specificStmt, sqlParser.AlterAddConstraintContext)):
            #Query: ALTER TABLE table_name ADD CONSTRAINT C
            #ALTER TABLE "table_name"ADD [CONSTRAINT_NAME] [CONSTRAINT_TYPE] [CONSTRAINT_CONDITION];
            #Prueba con: ALTER TABLE Customer ADD CONSTRAINT Con_First UNIQUE (Address);
            constraint = specificStmt.table_constraint().column_name()
            constraint2 = specificStmt.table_constraint().name()
            constraint_condition = constraint[0].getText()
            constraint_name = constraint2.getText()
            hello.addConstraint(self, oldName, constraint, constraint_condition, constraint_name)

        elif (isinstance(specificStmt, sqlParser.AlterDropColumnContext)):
            #Query: ALTER TABLE table_name DROP COLUMN nombre_columna
            hello.dropColumn(self, oldName, specificStmt.column_name().getText())

        elif (isinstance(specificStmt, sqlParser.AlterDropConstraintContext)):
            #Query: ALTER TABLE table_name DROP CONSTRAINT nombre_constraint
            hello.dropConstraint(self, oldName, specificStmt.name().getText())

    #ix) Borra una tabla 
    def enterDrop_table_stmt(self, ctx:sqlParser.Drop_table_stmtContext):
        #Query: DROP TABLE table_name;
        tableName = ctx.table_name().getText()
        print("¿Está seguro que desea borrar la tabla " + tableName+ "? (y/n)")
        respuesta = input()
        hello.dropTable(self, tableName, respuesta)

    #x) Muestra las tablas de la base de datos actual, si hay una en uso
    def enterShow_tables_stmt(self, ctx:sqlParser.Show_tables_stmtContext):
        #Query: show tables;
        hello.showTables(self)

    #xi) Muestra la descripción de columnas de una tabla 
    #    en la base de datos incluyendo las restricciones
    def enterShow_columns_stmt(self, ctx:sqlParser.Show_columns_stmtContext):
        #Query: SHOW COLUMNS FROM nombre;
        tableName = ctx.table_name().getText()
        hello.showColumns(self, tableName)

    def enterInsert_stmt(self, ctx:sqlParser.Insert_stmtContext):
        #Query: Insert into Table1 values(prueba,test)
        #Query: Insert into Table1(column1,column2) values(prueba,test)

        #Parametros
        tableName = ctx.table_name().getText()
        columnas = ctx.column_name()
        values = ctx.expr()
        
        hello.insert(self, tableName, columnas, values)

    #SELECT 
    def enterSelect_core(self, ctx:sqlParser.Select_coreContext):
        #Query: Select * from table_name;
        print("Entro al select")

    #Query: update hola set col1 = val1, col2 = val2 where ID = 1
    def enterUpdate_stmt(self, ctx:sqlParser.Update_stmtContext):
        col_list = ctx.column_name()
        for i in range(len(col_list)):
            print(col_list[i].getText())
        expr_list = ctx.expr()
        for i in range(len(expr_list)):
            print(expr_list[i].getText())
            if(i==len(expr_list)-1):
                where=expr_list[i].getText()
                print(where)
        print(ctx.table_name().getText())
        
    def enterDelete_stmt(self, ctx:sqlParser.Delete_stmtContext):
        #Query: delete from hola where id =1
        #Aca ctx.expr devuelve un solo valor en comparacion a otros que poseen una lista
        print(ctx.table_name().getText())
        try:
            print(ctx.expr().getText())
        except:
            print("Borrando todas las filas")
            column_list = hello.showColumns(self,ctx.table_name().getText())
            for i in range(len(column_list)):
                try:
                    hello.dropColumn(self,ctx.table_name().getText(),column_list[i])
                    hello.addColumn(self,ctx.table_name().getText(),column_list[i])
                except:
                    print("No se logro la operacion")
    def enterJoin_clause(self, ctx:sqlParser.Join_clauseContext):
    #Query: select * from tab1 left join tab2 on tab1.name = tab2.name
        tablaysub = ctx.table_or_subquery()
        for i in range(len(tablaysub)):
            print(tablaysub[i].getText())

        op_list = ctx.join_constraint()
        for i in range(len(op_list)):
            print(op_list[i].getText())

    

    
