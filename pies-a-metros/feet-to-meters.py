from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Pies a Metros")

# Estilo para cambiar el fondo
style = ttk.Style()
style.configure("TFrame", background="#FFBE0B")  # Fondo oscuro
style.configure("TLabel", background="#FFBE0B", foreground="#000814")  # Letras blancas
style.configure("TButton", background="#FFBE0B")  # Botón oscuro
style.map("TButton", background=[("active", "#FB5607")])  # Color al pasar el mouse

mainframe = ttk.Frame(root, padding="1 1 5 5")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

# feet_entry.configure(background="#1c1c1c", foreground="white", insertbackground="white")

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)

<<<<<<< HEAD
ttk.Label(mainframe, text="Ingrese la cantidad de pies: ").grid(column=1, row=1, sticky=W)
# ttk.Label(mainframe, text="Pies").grid(column=3, row=1, sticky=W)
=======
ttk.Label(mainframe, text="Pies").grid(column=3, row=1, sticky=W)
>>>>>>> 168135af427f8de40659d5f18930bb2745e5be28
ttk.Label(mainframe, text="es equivalente a: ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Metros").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()