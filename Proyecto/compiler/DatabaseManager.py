import os
import pathlib

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
            print("El nombre de la base de datos: " + oldName + " ha cambiado a: " + newName)
            oName.rename(directory + newName)
        else:
            print("No se realizaron los cambios")

    def showTables(self, db_name):
        tables = os.listdir('../Bases/' + db_name + '/')
        print (tables)
            
