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
                        print("La base de datos " + name + " ya existe, prueba con otro nombre")
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
                        print("La base de datos " + name + ' ya existe, prueba con otro nombre')
                else:
                    if not os.path.exists(directory2):
                        print('Creando json')
                        metadata = {}
                        metadata['bases'] = [] 
                        with open(directory2, 'w') as data:
                            json.dump(metadata, data)
                        print(metadata)
                    else:
                        print("La base de datos " + name + ' ya existe, prueba con otro nombre')
        except OSError:
                print ('Error: Creando directorio ' +  directory)


    def getDatabases(self):
        root = '../Bases/'
        print("Las bases de datos disponibles son: ")
        dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]
        #Recorre dirlist para imprimir cada base de datos existente
        for i in dirlist: 
            print(i)

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
            print("No se eliminó la base de datos" + name)
    
    def useDatabase(self, name): 
        global database
        directory = '../Bases/'
        ver = os.path.isdir(directory + name + '/')

        if (ver == True):
            database = name
            print("Ahora esta usando la base de datos " + database)
        else:
            print("La base de datos a la que desea acceder no existe")

    def createTable(self, name, columns, constraint):
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

            #CONSTRAINTS
            if (constraint != []): #Mientras existan los constraints
                i = 0
                while (i < len(constraint)): 
                    name = constraint[i].name().getText()
                    if constraint[i].K_PRIMARY() != None:
                        #print("PRIMARY " + name)
                        data['types'].append({
                            'column': name,
                            'type' : "PRIMARY"
                            })
                    elif constraint[i].K_FOREIGN() != None:
                        refer = constraint[i].foreign_key_clause().getText()
                        #print("FOREIGN " + name)
                        data['types'].append({
                            'column': name,
                            'type' : "FOREIGN KEY",
                            'reference' : refer
                            })
                    elif constraint[i].K_CHECK() != None: 
                        #print("CHECK " + name)
                        exp = constraint[i].expr().getText()
                        data['types'].append({
                            'column': name,
                            'type' : "CHECK",
                            'expresion' : exp
                            })
                    elif constraint[i].K_UNIQUE() != None:
                        #print("UNIQUE " + name)
                        col = constraint[i].getText()
                        data['types'].append({
                            'column': name,
                            'type' : "UNIQUE",
                            'colName' : col
                            })
                    i += 1

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
            data2['database'] = []
            data2['database'].append(
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
        global database
        print("Se agregara la columna " + column_name + " en la tabla " + table_name)
        tipos = '../Bases/'+ database +'/' + table_name + "types.json"
        
        with open(tipos) as col_file:
            cols = json.load(col_file)
        
        cols['types'].append({
            'column': column_name,
            'type': column_type
        })
        
        with open(tipos, 'w') as dataT:
            json.dump(cols, dataT)

        data = '../Bases/'+ database +'/' + table_name + ".json"
        
        with open(data) as json_file:
            tableD = json.load(json_file)
        
        dictTemp = {}
        cantReg = len(tableD['database'])
        for x in range (0,cantReg):
            dictTemp = tableD['database'].pop(0)
            dictTemp[column_name] = "NULL"
            tableD['database'].append(
                dictTemp
	        )
        
        with open(data, 'w') as dataD:
            json.dump(tableD, dataD)

    def addConstraint(self, table_name, constraint, cons_type, cons_name): 
        print(constraint + cons_type + cons_name)

    def dropColumn(self, table_name, column_name):
        global database
        print("Se eliminará la columna " + column_name + " de la tabla " + table_name)
        tipos = '../Bases/'+ database +'/' + table_name + "types.json"
        
        with open(tipos) as col_file:
            cols = json.load(col_file)
        
        for c in cols['types']:
            if (c['column'] == column_name):
                column_type = c['type']
        
        cols['types'].remove({
            'column': column_name,
            'type': column_type
        })
        
        with open(tipos, 'w') as dataT:
            json.dump(cols, dataT)

        data = '../Bases/'+ database +'/' + table_name + ".json"
        
        with open(data) as json_file:
            tableD = json.load(json_file)
        
        dictTemp = {}
        cantReg = len(tableD['database'])
        for x in range (0,cantReg):
            dictTemp = tableD['database'].pop(0)
            del dictTemp[column_name]
            tableD['database'].append(
                dictTemp
	        )
        
        with open(data, 'w') as dataD:
            json.dump(tableD, dataD)

    def dropConstraint(self, table_name, cons_name):
        print("Se eliminará el constraint " + cons_name + " de la tabla " + table_name)

    def showColumns(self, table_name): 
        global database
        column_list=[]
        i=0
        print("Las columnas de la tabla " + table_name + " son: ")
        tipos = '../Bases/' + database + '/' + table_name + "types.json"
        with open(tipos) as col_file:
            cols = json.load(col_file)
            for p in cols['types']:
                print(p['column'])
                column_list.append(p['column'])
                
        return column_list

    def insert(self, table_name, columns, values): 
        global database
        data = '../Bases/' + database + '/' + table_name + ".json"
        tipos = '../Bases/' + database + '/' + table_name + "types.json"
        arrCols = []
        
        with open(tipos) as col_file:
            cols = json.load(col_file)
            for p in cols['types']:
                arrCols.append(p['column'])
        cantCols = len(arrCols)
        
        numColss = len(columns)
        columnsF = []
        for col in range(0, numColss):
            columnsF.append(columns[col].getText())
        
        numVals = len(values)
        valuesF = []
        for v in range(0,numVals):
            valuesF.append(values[v].getText())

        for x in range(cantCols):
            if arrCols[x] not in columnsF:
                columnsF.append(arrCols[x])
                valuesF.append('NULL')
        numCols = len(columnsF)
        
        with open(data) as json_file:
            tableD = json.load(json_file)

        dictData = {}
        for y in range(0, numCols):
            dictData[columnsF[y]] = valuesF[y]

        for value in values:
            count3=0
            print(value.getText())
            try:
                if("." not in value.getText()):
                    int_value = int(value.getText())
                    print("es un entero")
                    count1=0
            except ValueError:
                print("No es un entero")
                count1=1
            try:
                float_value = float(value.getText())
                count2=0
            except ValueError:
                print("no es un float")
                count2=1
            try:
                if(value.getText().count('-')==2):
                    print("es una fecha")
                    fecha = value.getText()
                    separacion = fecha.split("-")
                    if(int(separacion[0])<=2018):
                        print("Año proporcionado es valido")
                        sub1=0
                    else:
                        print("El año ingresado supera el año actual")
                        sub1=1
                        count3=1
                    if(int(separacion[1])<=12 and int(separacion[1])>0):
                        print("el mes proporcionado es valido")
                        sub2=0
                    else:
                        print("El mes proporcionado no es valido")
                        sub2=1
                        count3=1
                    if(int(separacion[2])<=31 and int(separacion[2])>0):
                        print("el dia proporcionado es valido")
                        sub3=0
                    else:
                        print("El dia no es valido")
                        sub3=1
                        count3=1
                    if(sub1==0 and sub2==0 and sub3==0):
                        print("La fecha entera es valida")
                        count3=0
                else:
                    count3=1
                
            except ValueError:
                    print("no es una fecha")
            if(count1==1 and count2==1 and count3==1):
                print("El tipo de dato es char")
                
        
        
        tableD['database'].append(
            dictData
        )

        with open(data, 'w') as dataD:
            json.dump(tableD, dataD)
        
        print("Se realizaron los inserts en la tabla: " + table_name)

    def delete(self, table_name, expr):
        global database
        print("Se eliminará de la tabla " + table_name + " lo que cumpla con " + expr)
        #Split string expr
        exprSplit = expr.split('=')
        column_name = exprSplit[0]
        value = exprSplit[1]
        data = '../Bases/' + database + '/' + table_name + ".json"

        with open(data) as json_file:
            tableD = json.load(json_file)

        tableDA = {}
        tableDA['database'] = []

        for x in tableD['database']:
            if (x[column_name] != value):
                tableDA['database'].append(x)
            else:
                print(" ")
        with open(data, 'w') as dataD:
            json.dump(tableDA, dataD)

    def select(self, columns, tables, expr): 
        print(columns[0].getText())
        print(tables[0].getText())
        print(expr[0].getText())

    def update(self, columns, values, conditions, table_name):
        print("UPDATE en la tabla " + table_name)
        #Columns es el array de las columnas que desea cambiar
        for i in range(len(columns)):
            print(columns[i].getText())
        #Values es el array de los valores 
        for i in range(len(values)):
            print(values[i].getText())
        #Conditions el array de condiciones
        for i in conditions: 
            print(i)
