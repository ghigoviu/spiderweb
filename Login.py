from tkinter import *
#from tkinter.ttk import Entry
from ConexionBD import *
from tkinter import messagebox as mb

class Login(Frame):

    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        print("Iniciando Login")

        self.entryWidth = 22
        self.entryHeight = 5
        self.textH1 = "Calibri 13"
        self.textH2 = "Calibri 11"
        self.textH3 = "Calibri 9"

        #Definir elementos
        welcome = Label(self, text="Iniciando sesión\nIngrese sus datos", pady=15, font=self.textH1, padx=10)
        l1 = Label(self, text="Usuario:", pady=15, font=self.textH1, padx=10)
        l2 = Label(self, text="Contraseña:", pady=15, font=self.textH1, padx=10)
        self.user = Entry(self, font=self.textH1)
        self.passw = Entry(self, font=self.textH1)
        self.passw.config(show="*")
        boton = Button(self, text="Ingresar", width = 15, cursor = 'hand1',  font=self.textH1, pady=5,
                       command=lambda:controller.iniciarSesion(self.user.get(), self.passw.get()))

        #Acomodar elementos
        pad_y = 4
        welcome.pack()
        l1.pack()
        self.user.pack(pady=pad_y)
        l2.pack()
        self.passw.pack(pady=pad_y)
        boton.pack(pady=8)

    def show(self):
        self.mainloop()

    def ingresar(self, cadena, cadena2):
        print(cadena)
        print(cadena2)
        tipo = consultar_usuario(cadena, cadena2)
        if(tipo == 2):
            print("Consulta correcta: " + str(2) )
            #self.withdraw()
            #showAdmin()
        elif(tipo == 1):
            print("Consulta correcta: " + str(1) )
            #self.withdraw()
            #self.showTester()
        else:
            #print("Consulta incorecta" + str(tipo) )
            mb.showerror("Error de ingreso", "Usuario o contraseña incorrecta")


    def showTester(self):
        import MenuTester
        ventanaTester = MenuTester.MenuTester()
        ventanaTester.show()

    def pruebaT(self):
        print("Esta es una prueba para ver si funciona el enfoque a objetos con tkinter")
