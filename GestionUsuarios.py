#Menú del administrador

from tkinter import Frame
import tkinter
import tkinter.ttk
from tkinter import messagebox as mb
import ConexionBD as bd

class GestionUsuarios(Frame):

    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)


        #Definir elementos
        self.entryWidth = 15
        self.textH1 = "Calibri 13"
        self.textH2 = "Calibri 11"

        self.idUser = 0

        saludo = tkinter.Label(self, text="Puede consultar\nusuarios desde aquí:", pady=5, font=self.textH1)
        self.txtBuscar = tkinter.Entry(self, font=self.textH1, width= self.entryWidth)
        self.botonBuscar = tkinter.Button(self, text="Buscar", cursor='hand1', font=self.textH2, command= lambda: self.buscar())
        lblNombre = tkinter.Label(self, text="Nombre", pady=2, font=self.textH1)
        self.txtNombre = tkinter.Entry(self, font=self.textH1, width= self.entryWidth)
        lblTipo = tkinter.Label(self, text="Tipo", pady=2, font=self.textH1)
        self.txtTipo = tkinter.Entry(self, font=self.textH1, width= self.entryWidth)
        lblID = tkinter.Label(self, text="ID", pady=2, font=self.textH1)
        self.txtID = tkinter.Entry(self, font=self.textH1, width= self.entryWidth)
        botonEliminar = tkinter.Button(self, text="Eliminar", cursor='hand1', font=self.textH2,
                                        command= lambda: self.eliminar())
        botonGuardar = tkinter.Button(self, text="Guardar cambios", cursor='hand1', font=self.textH2,
                                        command= lambda: self.guardar())
        botonVolver = tkinter.Button(self, text="Volver", cursor='hand1', font=self.textH2,
                                        command= lambda: controller.showMenuAdmin())
        botonAgregar = tkinter.Button(self, text="Agregar nuevo", cursor='hand1', font=self.textH2,
                                        command= lambda: controller.showAgregarUser())

        #Acomodar elementos
        saludo.grid(row=0, column=0)
        self.txtBuscar.grid(row=1, column=0)
        self.botonBuscar.grid(row=1, column=1)
        lblNombre.grid(row=2, column=0)
        self.txtNombre.grid(row=2, column=1)
        lblTipo.grid(row=3, column=0)
        self.txtTipo.grid(row=3, column=1)
        lblID.grid(row=4, column=0)
        self.txtID.grid(row=4, column=1)
        botonGuardar.grid(row=5, column=1)
        botonEliminar.grid(row=6, column=0)
        botonAgregar.grid(row=6, column=1)
        botonVolver.grid(row=7, column=1)

    def buscar(self):
        self.txtNombre.delete(0, self.entryWidth)
        self.txtID.delete(0, self.entryWidth)
        self.txtTipo.delete(0, self.entryWidth)
        #Buscando elemento del txtBuscar
        usuarioDAO = bd.consultar_usuario_info(self.txtBuscar.get())
        if (usuarioDAO != None):
            self.txtNombre.insert(0, str(usuarioDAO.userr))
            self.txtID.insert(0, str(usuarioDAO.id))
            self.idUser = usuarioDAO.id
            if(usuarioDAO.tipo == 1):
                self.txtTipo.insert(0, "Tester")
            elif(usuarioDAO.tipo == 2):
                self.txtTipo.insert(0, "Admin")

    def eliminar(self):
        accept = mb.askokcancel("Advertencia", "¿Seguro que desea eliminar el elemento?")
        if(accept):
            print("Elemento eliminado")
            bd.eliminar_usuario(self.txtNombre.get())
        else:
            print("Elemento no eliminado")

    def agregar(self):
        print("Agregando nuevo elemento...")
        #from agregarUsuario import agregarUsuario
        # ventanaUsers= agregarUsuario()
        # ventanaUsers.show()

    def guardar(self):
        accept = mb.askokcancel("Advertencia", "¿Seguro que desea guardar los cambios?\nel campo ID no va a cambiar")
        if(accept):
            print("Guardando cambios")
            #usuario, tipo, id
            if (self.txtTipo.get() == "Tester") | (self.txtTipo.get() == "Admin"):
                bd.editar_usuario(self.txtNombre.get(), self.txtTipo.get(), self.idUser)
                mb.showinfo("Inserción correcta", "Cambios guardados correctamente")
        else:
            print("Cambios no guardados")



