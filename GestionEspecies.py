#Menú de arañas

import tkinter
import tkinter.ttk
from tkinter import Frame
from tkinter import messagebox as mb
import ConexionBD as bd
from PIL import Image, ImageTk
import PIL
import os

class GestionEspecies(Frame):

    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)


        self.entryWidth = 20
        self.entryHeight = 10
        self.textH1 = "Calibri 13"
        self.textH2 = "Calibri 11"
        self.textH3 = "Calibri 9"

        saludo = tkinter.Label(self, text="Puede consultar especies\n de arañas desde aquí:", pady=5, font=self.textH1)
        self.txtBuscar = tkinter.Entry(self, font=self.textH1, width= self.entryWidth)
        self.botonBuscar = tkinter.Button(self, text="Buscar", cursor='hand1', font=self.textH2,
                                          command= lambda: self.buscar())
        lblBinomial = tkinter.Label(self, text="Nombre binomial", pady=2, font=self.textH1)
        self.txtBinomial = tkinter.Entry(self, font=self.textH1, width= self.entryWidth)
        self.entryWidth += 10
        lblComunes = tkinter.Label(self, text="Otros nombres", pady=2, font=self.textH1)
        self.txtComunes = tkinter.Text(self, font=self.textH3, width= self.entryWidth, height = 3)
        lblTrat = tkinter.Label(self, text="Tratamientos", pady=2, font=self.textH1)
        self.txtTrat = tkinter.Text(self, font=self.textH3, width= self.entryWidth, height = self.entryHeight)
        lblZonas = tkinter.Label(self, text="Zonas", pady=2, font=self.textH1)
        self.txtZonas = tkinter.Text(self, font=self.textH3, width=self.entryWidth, height=self.entryHeight)
        #path = "C:\\Users\\Vrick\\Pictures\\Spiderweb_kb\\valid\\Seda_dorada\\2.jpg"
        #img = ImageTk.PhotoImage(Image.open(r'2.png').resize((100,100)))
        #lblImg = tkinter.Label(self, image = img)
        botonEliminar = tkinter.Button(self, text="Eliminar", cursor='hand1', font=self.textH2, command= lambda: self.eliminar())
        botonGuardar= tkinter.Button(self, text="Guardar", cursor='hand1', font=self.textH2, command= lambda: self.guardar())
        botonVolver = tkinter.Button(self, text="Volver", cursor='hand1', font=self.textH2, command= lambda: controller.showMenuAdmin())
        #botonAgregar = tkinter.Button(self, text="Agregar nuevo", cursor='hand1', font=self.textH2, command= lambda: self.agregar())

        #Acomodar elementos
        saludo.grid(row=0, column=0)
        self.txtBuscar.grid(row=1, column=0)
        self.botonBuscar.grid(row=1, column=1)
        lblBinomial.grid(row=2, column=0)
        self.txtBinomial.grid(row=3, column=0)
        lblComunes.grid(row=2, column=1)
        self.txtComunes.grid(row=3, column=1)
        lblTrat.grid(row=4, column=1)
        self.txtTrat.grid(row=5, column=1)
        botonEliminar.grid(row=6, column=0)
        #lblImg.grid(row=3, column=1)
        lblZonas.grid(row=4, column=0)
        self.txtZonas.grid(row=5, column=0)
        botonGuardar.grid(row=6, column=1)
        #botonAgregar.grid(row=7, column=1)
        botonVolver.grid(row=7, column=1)

    def buscar(self):
        self.txtBinomial.delete(0, self.entryWidth)
        self.txtZonas.delete('1.0', 'end')
        self.txtTrat.delete('1.0', 'end')
        self.txtComunes.delete('1.0', 'end')
        self.txtTrat.delete('1.0', 'end')
        i=0
        #Buscando elemento del txtBuscar
        try:
            especieDAO = bd.consultar_info_arana(self.txtBuscar.get())
            if (especieDAO != None):
                self.txtBinomial.insert(0, especieDAO.nombreC)
                nombres = bd.consultar_nombres_arana(especieDAO.id)
                for n in nombres:
                    self.txtComunes.insert('insert', n+'\n')
                    i += 1
                self.txtZonas.insert('insert', especieDAO.zonas)
                self.txtTrat.insert('insert', especieDAO.tratamientos)
        except :
            mb.showinfo("Error de búsqueda", "No se encontró ningún elemento")
            pass

    def guardar(self):
        if self.txtBuscar.get() != None:
            if bd.consultar_info_arana(self.txtBuscar.get()) != None:
                print("Editar información")
                accept = mb.askokcancel("Advertencia",
                                        "¿Seguro que desea guardar los cambios?" +
                                        "\nel campo Nombre Binomial no va a cambiar")
                if (accept):
                    bd.editar_especie(self.txtBinomial.get(), "",
                                   self.txtTrat.get("1.0","end-1c"), self.txtZonas.get("1.0","end-1c"))
                    print("Cambios guardados")
            else:
                print("Agregar información")
                accept = mb.askokcancel("Advertencia",
                                        "¿Seguro que desea guardar el registro?")
                if (accept):
                    bd.agregar_especie(self.txtBinomial.get(), "",
                                   self.txtTrat.get("1.0","end-1c"), self.txtZonas.get("1.0","end-1c"), self.txtBuscar.get())
                    mb.showinfo("Inserción correcta", "Registro guardado con éxito")

        else:
            mb.showinfo("Seleccione o introduzca un registro")

    def eliminar(self):
        accept = mb.askokcancel("Advertencia", "¿Seguro que desea eliminar el elemento?")
        if (accept):
            bd.eliminar_especie(self.txtBinomial.get())
            print("Elemento eliminado")
        else:
            print("Elemento no eliminado")