import os
import pathlib
import shutil

database = ""

class DatabaseManager:
        
    def createDatabase(self, name):
        directory = '../Bases/'+ name +'/'
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
                print ('Bases de datos' + name + 'creada')
        except OSError:
                print ('Error: Creating directory. ' +  directory)

    def getDatabases(self):
        bases = os.listdir('../Bases/')
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
            print("No existe la base de datos!")