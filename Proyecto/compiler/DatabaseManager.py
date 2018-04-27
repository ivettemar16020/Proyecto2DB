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

    def dropDatabase(self, name):
        directory = '../Bases/' + name + '/'
        shutil.rmtree(directory, ignore_errors=True)

    def useDatabase(self, name): 
        directory = '../Bases/'
        ver = os.path.isdir(directory + name + '/')

        if (ver == True):
            database = name
            print("Ahora esta usando la base de datos " + database)
        else:
            print("La base de datos a la que desea acceder no existe")

    def createTable(self, name, columns):
        directory2 = '../Bases/'+ database +'/' + "mData.json"
        arrColumns = []
        for column in columns: 
            arrColumns.append(column.column_name().getText())

        data = {}
        data[name] = []
        data[name].append({
            'column': arrColumns[0]
            })
        with open(directory2, 'w') as data1:
            json.dump(data, data1)
        print("Se creo la tabla " + name)

    def showTables(self, db_name):
        tables = os.listdir('../Bases/' + db_name + '/')
        print (tables)