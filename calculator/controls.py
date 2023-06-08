import tkinter as tk
from tkinter.font import Font

class Display(tk. Frame):
    def __init__(self,location):
        
        super().__init__(location, width=272, height=50)
        self.pack_propagate(False)
        
        self.label = tk.Label(self, background="#000000", text= "", foreground="#ffffff",
                              anchor=tk.E, padx=8, 
                              font=Font(family="Arial", size="40"))
        self.label.pack(side= tk.TOP, fill =tk.BOTH, expand=True)
    
    def typing(self, text):
        self.label.config(text=text)

    
class CalcButtom(tk. Frame):
    def __init__(self, location, tiny_wire, text):
        super().__init__(location, width= 68, height=50)
        self.pack_propagate(False)
        self.tiny_wire = tiny_wire
        self.text = text
        self.button = tk.Button(self, text=text, command=self.pressed)
        self.button.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def pressed(self):
        self.tiny_wire(self.text)

class Keyboard(tk.Frame):
    def __init__(self, location, tiny_wire):
        super().__init__(location, width=272, height=250)
        CalcButtom(self, tiny_wire, "AC").grid(column=0, row=0, columnspan=3, sticky='WENS')
        CalcButtom(self, tiny_wire, "÷").grid(column=3, row=0)
        CalcButtom(self, tiny_wire, "C").grid(column=0, row=1)
        CalcButtom(self, tiny_wire, "D").grid(column=1, row=1)
        CalcButtom(self, tiny_wire, "M").grid(column=2, row=1, rowspan=3, sticky='WENS')
        CalcButtom(self, tiny_wire, "x").grid(column=3, row=1)
        CalcButtom(self, tiny_wire, "X").grid(column=0, row=2)
        CalcButtom(self, tiny_wire, "L").grid(column=1, row=2)
        CalcButtom(self, tiny_wire, "-").grid(column=3, row=2)
        CalcButtom(self, tiny_wire, "I").grid(column=0, row=3)
        CalcButtom(self, tiny_wire, "V").grid(column=1, row=3)
        CalcButtom(self, tiny_wire, "+").grid(column=3, row=3)
        CalcButtom(self, tiny_wire, "=").grid(column=0, row=4, columnspan=4, sticky='WENS')
        
        
        


