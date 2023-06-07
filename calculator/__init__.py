import tkinter as tk
from .controls import Display, CalcButtom
WIDTH = 272
HEIGHT = 300
class Calculator(tk. Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry(f"{WIDTH}x{HEIGHT}")

        self.display = Display(self)
        self.display.pack()

        self.display.typing("Probando")

        CalcButtom(self, self.clic1, "1").pack()
        CalcButtom(self, text="2", tiny_wire=self.clic2).pack()
        CalcButtom(self, text="3", tiny_wire=self.clic3).pack()

    def clic1(self):
        self.display.typing("1")

    def clic2(self):
        self.display.typing("2")

    def clic3(self):
        self.display.typing("3")