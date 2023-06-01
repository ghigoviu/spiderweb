#Menú del administrador

from tkinter import *
import tkinter.ttk

class MenuAdmin(Frame):

    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.textH1 = "Calibri 13"
        self.textH2 = "Calibri 11"
        self.textH3 = "Calibri 9"
        self.spcY = 6

        saludo = tkinter.Label(self, text="Bienvenido de nuevo, \nelija una opción", pady=5, font=self.textH1)
        botonUsuarios = tkinter.Button(self, text="Gestionar Usuarios", width = 25, cursor = 'hand1',
                                        command= lambda: controller.showFUsers(), font=self.textH2)
        botonInfoA = tkinter.Button(self, text="Gestionar información \nde especies", width = 25, cursor = 'hand1',
                                        command= lambda: controller.showFSpiders(), font=self.textH2)
        botonReportes = tkinter.Button(self, text="Generar reportes de testing", width = 25, cursor = 'hand1',
                                        command= lambda: controller.showTestings(), font=self.textH2)
        botonRegresar = tkinter.Button(self, text="Salir", width = 10, cursor = 'hand1',
                                        command = lambda: controller.showInicio(), font=self.textH2)


        saludo.grid(row=0, column=0, pady=self.spcY)
        botonUsuarios.grid(row=1, column=0, pady=self.spcY, padx=20)
        botonInfoA.grid(row=2, column=0, pady=self.spcY)
        botonReportes.grid(row=3, column=0, pady=self.spcY)
        botonRegresar.grid(row=4, column=0, pady=self.spcY, padx=3)

    def gUsuarios(self):
        print("Entrando a gestion de usuarios")
        #ventanaUsers = gestionUsuarios()
        #ventanaUsers.show()
        #self.ventana.withdraw()

    def gEspecies(self):
        print("Entrando a gestion de especies")
    def gTesting(self):
        print("Entrando a historial de testing")


#menu = menuAdmin()
#menu.show()