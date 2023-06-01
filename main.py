# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as tk
from tkinter import ttk
from Login import Login
from MenuTester import MenuTester
from MenuAdmin import MenuAdmin
from Resultado import Resultado
from GestionEspecies import GestionEspecies
from GestionUsuarios import GestionUsuarios
from AgregarUsuario import AgregarUsuario
from AgregarEspecie import AgregarEspecie
from ReportesTesting import ReportesTesting

from ConexionBD import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("SpiderWeb v2.0")
        master = tk.Frame(self)
        master.pack()

        self.everyFrame = dict()
        self.tester = ""

        for F in (Resultado, Login, MenuTester, MenuAdmin, ReportesTesting,
                  GestionEspecies, GestionUsuarios, AgregarUsuario, AgregarEspecie):
            print("*")
            frame = F(master, self)
            self.everyFrame[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.showFrame(Login)

    def showAgregarUser(self):
        print("Mostrando ventana de agregar usuario")
        self.showFrame(AgregarUsuario)

    def showResultado(self, path):
        pathImg = self.everyFrame[MenuTester].file_name
        frame = self.everyFrame[Resultado]
        frame.setPath(pathImg)
        frame.tkraise()

    def showMenuTester(self):
        print("Mostrando ventana de tester")
        self.showFrame(MenuTester)

    def showMenuAdmin(self):
        print("Mostrando ventana de admin")
        self.showFrame(MenuAdmin)

    def showFUsers(self):
        print("Mostrando ventana de gestión de usuarios")
        self.showFrame(GestionUsuarios)

    def showFSpiders(self):
        print("Mostrando ventana de gestión de especies")
        self.showFrame(GestionEspecies)

    def showTestings(self):
        print("Mostrando ventana de reportes de testing")
        self.showFrame(ReportesTesting)

    def showMenuTestings(self):
        print("Mostrando ventana de reportes de testing")
        #self.showFrame(ReportesTesting)

    def showAddEspecie(self):
        print("Mostrando ventana de reportes de testing")
        self.showFrame(AgregarEspecie)

    def showInicio(self):
        print("Mostrado ventana de inicio")
        self.showFrame(Login)

    def showFrame(self, contenedorLlamado):
        print("Mostrando Frames")
        frame = self.everyFrame[contenedorLlamado]
        frame.tkraise()

    def iniciarSesion(self, usuario, password):
        print(usuario)
        print(password)
        tipo = consultar_usuario(usuario, password)
        if (tipo == 2):
            print("Consulta correcta: " + str(2) )
            self.showFrame( MenuAdmin )
        elif (tipo == 1):
            print("Consulta correcta: " + str(1) )
            self.showFrame( MenuTester)
            self.everyFrame.get(MenuTester).setUsuario(usuario)
            self.setTester(usuario)
        else:
            print("Consulta incorecta" + str(tipo) )
            mb.showerror("Error de ingreso", "Usuario o contraseña incorrecta")

    def setTester(self, nombreTester):
        self.tester = nombreTester

    def getTester(self):
        return self.tester




if __name__ == '__main__':
    print_hi('PyCharm')
    root = Main()
    root.mainloop()
