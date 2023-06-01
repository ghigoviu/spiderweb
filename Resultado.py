#Resultado de la predicción

from tkinter import Tk, Button, Label, Frame, RIGHT
from Prediccion import *
import ConexionBD as bd


class Resultado(Frame):

    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)


        self.entryWidth = 18
        self.entryHeight = 5
        self.textH1 = "Calibri 13"
        self.textH2 = "Calibri 11"
        self.textH3 = "Calibri 9"
        self.path = ""
        self.resultado = "Viuda neg"


        #Definir elementos
        self.encabezado = Label(self, text="Resultado obtenido", pady=5, font=self.textH1)
        self.botones = Frame(self)
        self.lblPregunta = Label(self.botones, text="¿El resultado es correcto?", pady=5, font=self.textH1)
        self.lblResult = Label(self, pady=5, font=self.textH1)
        self.lblRecom = Label(self, pady=5, font=self.textH1)
        self.botonRegresar = Button(self, text="Volver", width = 10, cursor = 'hand1',
                                            command = lambda: controller.showMenuTester(), font=self.textH2)
        self.spcY = 6
        self.spcY = 6
        self.encabezado.pack(pady=self.spcY, padx=10)

        #self.lblPregunta.pack()

        self.botonSi = Button(self.botones, text="Si", width=5, cursor='hand1',
                                      command=lambda: self.sip(controller.getTester()), font=self.textH2)
        self.botonNo = Button(self.botones, text="No", width=5, cursor='hand1',
                                      command=lambda: self.nop(controller.getTester()), font=self.textH2)

        #Acomodando elementos
        self.lblResult.pack()
        self.lblRecom.pack()
        self.lblPregunta.pack()
        self.botonSi.pack(side=RIGHT)
        self.botonNo.pack(side='left')
        self.botones.pack()
        self.botonRegresar.pack(pady=self.spcY, padx=3)

    def nop(self, user):
        print("No")
        bd.evaluarResultado(self.path, self.resultado, 0, user)

    def sip(self, user):
        print("Si")
        bd.evaluarResultado(self.path, self.resultado, 1, user)

    def setPath(self, path):
        self.path = path
        self.resultado = predict(path)
        #self.lblResult.config(text= "Por ahora solo probamos")
        self.lblRecom.config(text= bd.consultar_tratamientos(self.resultado), wraplength=500)
        self.lblResult.config(text= self.resultado)

