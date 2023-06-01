#Menú del tester

from tkinter import *
from tkinter import filedialog, Label
from PIL import Image, ImageTk as itk


class MenuTester(Frame):

    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.entryWidth = 22
        self.entryHeight = 5
        self.textH1 = "Calibri 13"
        self.textH2 = "Calibri 11"
        self.textH3 = "Calibri 9"
        self.usuario = ""
        self.boton = Button(self, text="Cargar imagen", width = 12, cursor = 'hand1',  font=self.textH2, pady=5, command=self.load)
        lblsaludo = Label(self, text="Probando la red neuronal\n", pady=10, font=self.textH1, padx=10)
        #self.txtBuscar = Entry(self.ventana, font=self.textH1, width=self.entryWidth)
        file = "C:/Users/Vrick/Desktop/Pruebas/GB134.jpg"
        img = itk.PhotoImage(file=file)
        self.lbl_imagen = Label(self, image=img)
        lblsaludo.pack(padx=15)
        self.boton.pack()
        self.lbl_imagen.pack()
        botonMostrar = Button(self, text="Evaluar", width = 12, cursor = 'hand1',  font=self.textH2, pady=5,
                                command=lambda: controller.showResultado(self.file_name))
        botonSi = Button(self, text="Si", width = 5, cursor = 'hand1', font=self.textH2)
        botonNo = Button(self, text="No", width = 5, cursor = 'hand1', font=self.textH2)
        botonSalir = Button(self, text="Salir", width = 12, cursor = 'hand1',
                                command = lambda: controller.showInicio(),  font=self.textH2, pady=5)
        '''''
        saludo.grid(row=0, column=0)

        botonUsuarios.grid(row=1, column=0)
        botonInfoA.grid(row=2, column=0)
        botonReportes.grid(row=3, column=0)
        botonRegresar.grid(row=3, column=1)
        '''
        self.spcY = 8

        #self.txtBuscar.pack()
        botonMostrar.pack(pady=self.spcY, padx = 20)
        botonSalir.pack(pady=self.spcY)

    def setUsuario(self, usuario):
        self.usuario = usuario

    def load(self):
        self.file_name=filedialog.askopenfilename(title='Subir', filetypes=[('JPG FILES', '*.jpg')])

        pil_img = Image.open(self.file_name)
        wh = int(pil_img.width/2)
        pil_img = pil_img.resize((wh, wh), Image.ANTIALIAS)
        pil_img = itk.PhotoImage(pil_img)

        self.lbl_imagen.config(image=pil_img)
        self.lbl_imagen.image=pil_img  # Recomendación de la documentación de PhotoImage

    def setUser(self, nombreUsuario):
        self.usuario = nombreUsuario
        print("Abriendo menu para el usuario " + nombreUsuario)

    def mostrar(self):
        print("Mostrando imagen")

    def salir(self):
        self.quit()

    def showResultado(self):
        self.evaluar = Toplevel(self.master)
        #Resultado(self, self.file_name)


#menu = MenuTester(Tk, Frame)
#menu.show()


