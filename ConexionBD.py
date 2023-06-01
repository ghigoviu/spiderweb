#Funcionalidades de base de datos

from peewee import MySQLDatabase, Model, TextField, IntegerField, AutoField, ForeignKeyField
from tkinter import messagebox as mb

NOMBRE_BASE_DE_DATOS = "webspider"
USUARIO = "root"
PALABRA_SECRETA = ""
conexion = MySQLDatabase(NOMBRE_BASE_DE_DATOS, user=USUARIO, password=PALABRA_SECRETA)
title = "Conexion a BD"

class ModeloBase(Model):
    class Meta:
        database = conexion

class Usuario(ModeloBase):
    id = AutoField()
    tipo = IntegerField()
    userr = TextField()
    password = TextField()

class Especies(ModeloBase):
    id = AutoField()
    nombreC = TextField()
    descripcion = TextField()
    tratamientos = TextField()
    zonas = TextField()

class NombresComunes(ModeloBase):
    id = AutoField()
    nombre = TextField()
    especie_id = ForeignKeyField(Especies)

class Imagen(ModeloBase):
    id = AutoField()
    ruta = TextField()
    especie = ForeignKeyField(Especies)

class Test(ModeloBase):
    id = AutoField()
    inputt = TextField()
    outputt = TextField()
    calif = IntegerField()
    especie_resultado = ForeignKeyField(Especies)
    usuario_id = ForeignKeyField(Usuario)

#Creando CRUDS
def getLastEspecie():
     id = Especies.select(Especies.id).order_by(Especies.id)
     return id[-1]

def agregar_especie(nombreB, desc, trat, zones, name):
    Especies.create(nombreC=nombreB, descripcion=desc, tratamientos=trat, zonas=zones)
    NombresComunes.create(nombre=name, especie_id = getLastEspecie())
    print("Creación correcta")

def editar_especie(nombreB, desc, trat, zones):
    Especies.update({Especies.tratamientos: trat}).where(Especies.nombreC == nombreB).execute()
    Especies.update({Especies.zonas: zones}).where(Especies.nombreC == nombreB).execute()
    Especies.update({Especies.descripcion: desc}).where(Especies.nombreC == nombreB).execute()
    print("Cambios realizados correctamente")

def eliminar_especie(name):
    print(NombresComunes.delete().where(NombresComunes.especie_id == Especies.get(Especies.nombreC == name).id ).execute())
    print(Especies.delete().where(Especies.nombreC == name).execute())
    print("Especie " + name + " eliminada")



def agregar_usuario(user, passw, tipo):
    if consultar_usuario_info(user) == None:
        Usuario.create(userr = user, password = passw, tipo = tipo)
        print("Creación correcta")
        return 1
    elif consultar_usuario_info(user) != None:
        mb.showwarning("Error de inserción", "Usuario ya registrado, elija otro nombre")
        return 0

def consultar_usuario(usuario, passw):
    try:
        user = Usuario.get(Usuario.userr == usuario)
        pw = Usuario.get(Usuario.userr == usuario).password
        if(passw == pw):
            #Contraseña correcta
            tipo = Usuario.get(Usuario.userr == usuario).tipo
            if (tipo == 1):
                return 1
            elif (tipo == 2):
                return 2
        else:
            print("Contraseña incorrecta")
            return 0
    except:
        mb.showerror(title, "Usuario no encontrado")
        pass

def consultar_usuario_info(usuario):
    try:
        user = Usuario.get(Usuario.userr == usuario)
        return user
    except:
        mb.showerror(title, "Usuario no encontrado")
        return None
        pass

def usuariosTester():
    #print("Obteniendo todos los nombres del id " + str(id_especie))
    query = (Usuario.select().where(Usuario.tipo == 1))
    namess = []
    for name in query:
        # print(name.nombre)
        namess.append(name.userr)
    return namess

def testUsers(usuario):
    user_id = consultar_usuario_info(usuario).id
    q = (Test.select().where(Test.usuario_id == user_id))
    print(q)
    test = []
    for i in q:
        test.append(i)
    return test

def editar_usuario(us, tp, id):
    Usuario.update({Usuario.userr: us}).where(Usuario.id == id).execute()
    if (tp == "Admin"):
        Usuario.update({Usuario.tipo: 2}).where(Usuario.id == id).execute()
    elif (tp == "Tester"):
        Usuario.update({Usuario.tipo: 1}).where(Usuario.id == id).execute()
    print("Usuario actualizado con éxito")

def eliminar_usuario(us):
    Usuario.delete().where(Usuario.userr == us).execute()
    print("Usuario " + us + " eliminado")

def consultar_info_arana(nombr):
    #print("Ejecutando consulta de araña " + nombr)
    query = (NombresComunes.select().where(NombresComunes.nombre == nombr))
    #if query is not None:
    try:
        nam = query[0]
        return Especies.get_by_id(nam.especie_id)
    #else:
    except:
        return None

def consultar_tratamientos(nombr):
    query = (NombresComunes.select().where(NombresComunes.nombre == nombr))
    if query is not None:
        nam = query[0]
        print(nam)
        return Especies.get_by_id(nam.especie_id).tratamientos
    else:
        return None

def consultar_nombres_arana(id_especie):
    print("Obteniendo todos los nombres del id " + str(id_especie))
    query = (NombresComunes.select().where(NombresComunes.especie_id == id_especie))
    namess = []
    for name in query:
        #print(name.nombre)
        namess.append(name.nombre)
    return namess

def evaluarResultado(path, resultado, calf, user):
    print("Insertando la evaluación del sistema")
    us = consultar_usuario_info(user).id
    registroTest = Test(
        inputt = path,
        outputt = resultado,
        calif = calf,
        usuario_id = us
    )
    registroTest.save()
    print("Creado registro de test correctamente")


#print(testUsers("R"))

#print(usuariosTester())
#agregar_especie("A", "B", "C", "Z", "Y")
print(getLastEspecie())
