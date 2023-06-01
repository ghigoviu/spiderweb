#Agregar usuario a la base de datos

from tkinter import Frame
import tkinter
import tkinter.ttk
from tkinter import messagebox as mb
import ConexionBD as bd

class AgregarUsuario(Frame):

    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        #Definir elementos
        self.entryWidth = 15
        self.spcY = 6
        self.textH1 = "Calibri 13"
        self.textH2 = "Calibri 11"

        opcTipos = ["Administrador", "Tester"]
        saludo = tkinter.Label(self, text="Ingrese información de nuevo usuario", pady=5)
        lblNombre = tkinter.Label(self, text="Nombre", pady=2)
        self.txtNombre = tkinter.Entry(self, font=self.textH1, width= self.entryWidth)
        lblTipo = tkinter.Label(self, text="Tipo", pady=2)
        self.txtTipo = tkinter.Entry(self, font=self.textH1, width= self.entryWidth)
        self.cmbTipo = tkinter.Listbox(self, font=self.textH1, width= self.entryWidth, height=2)
        self.cmbTipo.insert(0, opcTipos[0])
        self.cmbTipo.insert("end", opcTipos[1])
        lblID = tkinter.Label(self, text="Contraseña", pady=2)
        self.txtPassw = tkinter.Entry(self, font=self.textH1, width= self.entryWidth)
        botonAgregar = tkinter.Button(self, text="Agregar nuevo", cursor='hand1',
                                      command=lambda: self.agregar())
        botonVolver = tkinter.Button(self, text="Volver", cursor='hand1',
                                      command=lambda: controller.showMenuAdmin() )
        #Acomodar elementos
        saludo.grid(row=0, column=0, pady= self.spcY)
        lblNombre.grid(row=1, column=0, pady= self.spcY)
        self.txtNombre.grid(row=1, column=1, pady= self.spcY)
        lblTipo.grid(row=2, column=0, pady= self.spcY)
        self.cmbTipo.grid(row=2, column=1, pady= self.spcY)
        lblID.grid(row=3, column=0, pady= self.spcY)
        self.txtPassw.grid(row=3, column=1, pady= self.spcY)
        botonAgregar.grid(row=4, column=1, pady= self.spcY)
        botonVolver.grid(row=5, column=1, pady= self.spcY)


    def agregar(self):
        print("Agregando nuevo elemento...")
        name = self.txtNombre.get()
        #type = self.txtTipo.get()
        passw = self.txtPassw.get()
        try:
            type = self.cmbTipo.selection_get()
            if(str(type) == "Administrador"):
                tpe = 2
                bd.agregar_usuario(name, passw, tpe)
                print("Elemento agregado correctamente")
                mb.showinfo("Inserción exitosa", "El elemento se ha agregado correctamente")
            elif(str(type) == "Tester"):
                tpe = 1
                if bd.agregar_usuario(name, passw, tpe) == 1:
                    mb.showinfo("Inserción exitosa", "El elemento se ha agregado correctamente")
                else:
                    print("Elemento no agregado")
                    #mb.showerror("Inserción fallida", "El elemento no se ha agregado correctamente")
        except:
            mb.showerror("Error de inserción", "Por favor, indique el tipo de usuario")
            pass

