import tkinter as tk

def imprimir_saludo():
    label.config(text=f"Hola, {valor_nombre.get()}")#sin el get no nos daria el valor de la variable

root = tk.Tk() #Contenedor principal/pantalla
root.title("Mi primera pantalla tkinter")

root.geometry("800x600+100+200")

label = tk.Label(root, text="", bd=2, relief=tk.RAISED, width=50)
label.pack()

#label1 = tk.Label(root, text= "Y ahora otra label")
#label.pack()
#label1.pack(side=tk.LEFT)

valor_nombre = tk.StringVar() # Es una clase de kinter q es una variable de control

nombre = tk.Entry(root, textvariable=valor_nombre) # input
nombre.pack()

boton = tk.Button(root, text="Pulsame", command=imprimir_saludo)
boton.pack() #Hace que salga en pantalla de forma pack

root.mainloop()
