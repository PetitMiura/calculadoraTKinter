import tkinter as tk

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__() #Necesitamos llamar el init de tk
        self.title("Mi primera pantalla tkinter") # El root se convierte en self directamente
        self.geometry("800x600+400+200")
        self.label = tk.Label(self, text="", bd=2, relief=tk.RAISED, width=50)
        self.label.pack()
        self.valor_nombre = tk.StringVar()
        nombre = tk.Entry(self, textvariable=self.valor_nombre) # input q se va a usar 1 sola vez
        nombre.pack()
        boton = tk.Button(self, text="Pulsame", command=self.imprimir_saludo)
        boton.pack() #Hace que salga en pantalla de forma pack

    def imprimir_saludo(self):
        self.label.config(text=f"Hola, {self.valor_nombre.get()}")

#Ventana().mainloop() #"hazemos que se instancie" 