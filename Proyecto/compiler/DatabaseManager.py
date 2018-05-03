import os
import pathlib
import shutil
import json

database = ""

class DatabaseManager:
        
    def createDatabase(self, name):
        directory = '../Bases/'+ name +'/'
        directory1 = '../Bases/'
        directory2 = '../Bases/'+ name +'/' + "mData.json"
        try:
            if not os.path.exists(directory1):
                os.makedirs(directory1)
                print("Bases no existe, se esta creando")
                if not os.path.exists(directory):
                    os.makedirs(directory)
                    print ('Bases de datos ' + name + ' creada')
                    if not os.path.exists(directory2):
                        print('Creando json')
                        metadata = {}
                        metadata['bases'] = [] 
                        with open(directory2, 'w') as data:
                            json.dump(metadata, data)
                        print(metadata)
                    else:
                        print(name + ' ya existe, prueba con otro nombre')
            else: 
                if not os.path.exists(directory):
                    os.makedirs(directory)
                    print ('Bases de datos ' + name + ' creada')
                    if not os.path.exists(directory2):
                        print('Creando json')
                        metadata = {}
                        metadata['bases'] = [] 
                        with open(directory2, 'w') as data:
                            json.dump(metadata, data)
                        print(metadata)
                    else:
                        print(name + ' ya existe, prueba con otro nombre')
                else:
                    if not os.path.exists(directory2):
                        print('Creando json')
                        metadata = {}
                        metadata['bases'] = [] 
                        with open(directory2, 'w') as data:
                            json.dump(metadata, data)
                        print(metadata)
                    else:
                        print(name + ' ya existe, prueba con otro nombre')
        except OSError:
                print ('Error: Creando directorio ' +  directory)


    def getDatabases(self):
        bases = os.listdir('../Bases/')
        print("Las bases de datos disponibles son: ")
        for base in bases: 
            print(base)

    def alterDatabase(self, oldName, newName, res): 
        directory = '../Bases/'
        oName = pathlib.Path(directory + oldName)

        if (res == "y"):
            oName.rename(directory + newName)
            print("El nombre de la base de datos: " + oldName + " ha cambiado a: " + newName)   
        else:
            print("No se realizaron los cambios")

    def dropDatabase(self, name, res):
        directory = '../Bases/' + name + '/'
        if (res == "y"):
            shutil.rmtree(directory, ignore_errors=True)
            print("La base de datos " + name + " ha sido eliminada")  
        else:
            print("No se elimino la base de datos" + name)
    
    def useDatabase(self, name): 
        global database
        directory = '../Bases/'
        ver = os.path.isdir(directory + name + '/')

        if (ver == True):
            database = name
            print("Ahora esta usando la base de datos " + database)
        else:
            print("La base de datos a la que desea acceder no existe")

    def createTable(self, name, columns):
        global database
        if (database != ''):  
            arrColumns = []
            arrTypes = []
            for column in columns: 
                arrColumns.append(column.column_name().getText())
                arrTypes.append(column.type_name().getText())

            datadir = '../Bases/'+ database +'/' + name + ".json"
            typedir = '../Bases/'+ database +'/' + name + "types.json"

            numCols = len(arrColumns)

            data = {}
            data['types'] = []
            for x in range(0, numCols):
                data['types'].append({
                    'column': arrColumns[x],
                    'type' : arrTypes[x]
                })

            with open(typedir, 'w') as dataT:
                json.dump(data, dataT)

            dictCols = {}
            for y in range(0, numCols):
                dictCols[arrColumns[y]] = ''

            data2 = {}
            data2[name] = []
            data2[name].append(
                dictCols
            )
            
            with open(datadir, 'w') as dataD:
                json.dump(data2, dataD)
            
            print("Se creo la tabla " + name)
        else: 
            print("\nERROR\nDebes seleccionar una base de datos para poder realizar esta acción")
            print("Prueba utilizando 'use database dbName'")

    def showTables(self):
        global database
        if (database != ''):
            tables = os.listdir('../Bases/' + database + '/')
            print ("Las tablas existentes en " + database + " son: ")
            for table in tables:
                print(table)
        else: 
            print("\nERROR\nDebes seleccionar una base de datos para poder realizar esta acción")
            print("Prueba utilizando 'use database dbName'")

    def dropTable(self, table_name, respuesta): 
        global database
        if (database != ''):
            datadir = '../Bases/'+ database +'/' + table_name + ".json"
            typedir = '../Bases/'+ database +'/' + table_name + "types.json"
            
            if respuesta == "y": 
                os.remove(datadir)
                os.remove(typedir)
                print ("La tabla '" + table_name + "' ha sido eliminada exitosamente")
            else: 
                print("La tabla '" + table_name + "' no ha sido eliminada")
        else: 
            print("\nERROR\nDebes seleccionar una base de datos para poder realizar esta acción")
            print("Prueba utilizando 'use database dbName'")

    def alterTabName(self, old_name, new_name): 
        global database
        if (database != ''):
            datadir = '../Bases/'+ database +'/' + old_name + ".json"
            typedir = '../Bases/'+ database +'/' + old_name + "types.json"
            newName = '../Bases/'+ database +'/' + new_name + ".json"
            newTypeName = '../Bases/'+ database +'/' + new_name + "types.json"
            os.rename(datadir, newName)
            os.rename(typedir, newTypeName)
            print("La tabla " + old_name + " ha cambiado a " + new_name)
        else: 
            print("\nERROR\nDebes seleccionar una base de datos para poder realizar esta acción")
            print("Prueba utilizando 'use database dbName'")


    def addColumn(self, table_name, column_name, column_type): 
        print("Se agregara la columna " + column_name + " en la tabla " + table_name)

    def addConstraint(self, table_name, constraint, cons_type, cons_name): 
        print(constraint + cons_type + cons_name)

    def dropColumn(self, table_name, column_name):
        print("Se eliminará la columna " + column_name + " de la tabla " + table_name)

    def dropConstraint(self, table_name, cons_name):
        print("Se eliminará el constraint " + cons_name + " de la tabla " + table_name)

    def showColumns(self, table_name): 
        global database
        print("Las columnas de la tabla " + table_name + " son: ")
        tipos = '../Bases/' + database + '/' + table_name + "types.json"
        with open(tipos) as col_file:
            cols = json.load(col_file)
            for p in cols['types']:
                print(p['column'])

    def insert(self, table_name, columns, values): 
        print("Se realizaran los inserts en la tabla: " + table_name)
        
        for column in columns:
            print(column.getText()) 

        for value in values: 
            print(value.getText())