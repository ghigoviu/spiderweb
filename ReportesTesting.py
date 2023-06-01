#Reportes de testing

from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Treeview
import ConexionBD as bd


class ReportesTesting(Frame):

    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.entryWidth = 15
        self.textH1 = "Calibri 13"
        self.textH2 = "Calibri 11"
        self.textH3 = "Calibri 9"
        self.spcY = 6

        opcTesters = bd.usuariosTester()

        saludo = Label(self, text="Generando reportes de testing\nSelecione un nombre:", pady=5, font=self.textH1)
        self.cmbName = Listbox(self, font=self.textH1, width=self.entryWidth, height=2)
        for i in opcTesters:
            self.cmbName.insert("end", i)
        btnMostrar = Button(self, text="Mostrar", cursor='hand1', font=self.textH2,
                                      command=lambda: self.mostrarSelect())
        btnVolver = Button(self, text="Volver", cursor='hand1', font=self.textH2,
                                     command=lambda: controller.showMenuAdmin())

        self.tabla = Treeview(self, columns=3)
        self.lblAccuracy = Label(self)

        saludo.pack(pady=self.spcY)
        self.cmbName.pack(pady=self.spcY)
        btnMostrar.pack(pady=self.spcY)
        btnVolver.pack(pady=self.spcY)

        self.tabla.pack(pady=self.spcY)
        self.tabla.heading("#0", text="Resultado", anchor=CENTER)
        self.tabla.heading("#1", text="Imagen", anchor=CENTER)

    def mostrarSelect(self):
        self.tabla.delete(*self.tabla.get_children())
        query = bd.testUsers(self.cmbName.selection_get() )
        total = 0
        acc = 0
        for (test) in query:
            self.tabla.insert('', 0, text=(test.outputt + " " + self.st(test.calif)), values=test.inputt)
            total += 1
            if test.calif == 1:
                acc += 1
        try:
            total = acc/total
        except:
            mb.showinfo("Consulta vacía", " No hay registros de este usuario")
        print("Precición del " + str(total) + " %" )
        mb.showinfo("Mostrnado presición", "Precición del " + str(total) + " %" )
        return "Precición del " + str(total) + " %"


    def st(self, c):
        if c == 1:
            return "(Correcta)"
        else:
            return "(Incorrecta)"