# import tkinter as tk
# from tkinter import font

# # Colores
# BG_COLOR = "#2E3440"
# BTN_COLOR = "#4C566A"
# BTN_TEXT_COLOR = "#ECEFF4"
# ENTRY_BG = "#3B4252"
# ENTRY_TEXT_COLOR = "#FFFFFF"
# HIGHLIGHT_COLOR = "#88C0D0"
# ERROR_COLOR = "#BF616A"
# SUCCESS_COLOR = "#A3BE8C"

# # Función para actualizar la entrada
# def press(symbol):
#     entry.configure(bg=ENTRY_BG)  # reset fondo si estaba en error
#     current = entry_var.get()
#     entry_var.set(current + str(symbol))
#     animate_entry_blink(SUCCESS_COLOR)

# # Calcular resultado
# def equal():
#     try:
#         result = eval(entry_var.get())
#         entry_var.set(str(result))
#         animate_entry_blink(SUCCESS_COLOR)
#     except Exception:
#         entry_var.set("Error")
#         animate_entry_blink(ERROR_COLOR)

# # Limpiar entrada
# def clear():
#     entry_var.set("")
#     entry.configure(bg=ENTRY_BG)

# # Animación de "parpadeo"
# def animate_entry_blink(color):
#     entry.configure(bg=color)
#     root.after(150, lambda: entry.configure(bg=ENTRY_BG))

# # Efecto visual para los botones
# def animate_button(btn):
#     original_color = btn["bg"]
#     btn.configure(bg=HIGHLIGHT_COLOR)
#     root.after(100, lambda: btn.configure(bg=original_color))

# # Ventana principal
# root = tk.Tk()
# root.title("Calculadora Fachera")
# root.geometry("320x420")
# root.configure(bg=BG_COLOR)
# root.resizable(False, False)

# # Fuente
# app_font = font.Font(family="Helvetica", size=18, weight="bold")

# # Entrada
# entry_var = tk.StringVar()
# entry = tk.Entry(root, textvariable=entry_var, font=app_font, bg=ENTRY_BG,
#                  fg=ENTRY_TEXT_COLOR, bd=0, justify="right", insertbackground=ENTRY_TEXT_COLOR)
# entry.pack(fill="both", padx=10, pady=20, ipady=15)

# # Botones
# buttons = [
#     ("7", "8", "9", "/"),
#     ("4", "5", "6", "*"),
#     ("1", "2", "3", "-"),
#     ("C", "0", "=", "+"),
# ]

# def create_button(text, row, col):
#     action = lambda: handle_press(text)
#     btn = tk.Button(root, text=text, font=app_font,
#                     bg=BTN_COLOR, fg=BTN_TEXT_COLOR, activebackground=HIGHLIGHT_COLOR,
#                     activeforeground=ENTRY_TEXT_COLOR, bd=0, command=lambda: [action(), animate_button(btn)])
#     btn.place(x=col*80+10, y=row*80+100, width=70, height=70)
#     return btn

# def handle_press(text):
#     if text == "=":
#         equal()
#     elif text == "C":
#         clear()
#     else:
#         press(text)

# for i, row in enumerate(buttons):
#     for j, btn_text in enumerate(row):
#         create_button(btn_text, i, j)

# # Ejecutar
# root.mainloop()

import customtkinter as ctk

# Inicializar ventana
ctk.set_appearance_mode("dark")  # Puedes cambiar a "light"
ctk.set_default_color_theme("blue")  # También podés crear tu propio theme

app = ctk.CTk()
app.title("Calculadora Fachera")
app.geometry("320x420")
app.resizable(False, False)

# Colores
PRIMARY = "#C0E83E"
SECONDARY = "#5C349E"
ERROR_COLOR = "#BF616A"
SUCCESS_COLOR = "#A3BE8C"
ENTRY_BG = "#3B4252"

# Variable de entrada
entry_var = ctk.StringVar()

# Entrada
entry = ctk.CTkEntry(app, textvariable=entry_var, font=("Helvetica", 24),
                     justify="right", height=60, fg_color=ENTRY_BG, text_color="white")
entry.pack(padx=10, pady=20, fill="x")

# Funciones
def press(symbol):
    entry.configure(fg_color=ENTRY_BG)
    entry_var.set(entry_var.get() + str(symbol))

def clear():
    entry_var.set("")
    entry.configure(fg_color=ENTRY_BG)

def equal():
    try:
        result = eval(entry_var.get())
        entry_var.set(str(result))
        animate_entry_flash(SUCCESS_COLOR)
    except:
        entry_var.set("Error")
        animate_entry_flash(ERROR_COLOR)

def animate_entry_flash(color):
    entry.configure(fg_color=color)
    app.after(150, lambda: entry.configure(fg_color=ENTRY_BG))

# Crear botones
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+"),
]

def create_button(text, row, col):
    def handle():
        if text == "=":
            equal()
        elif text == "C":
            clear()
        else:
            press(text)

    btn = ctk.CTkButton(app, text=text, command=handle,
                        width=70, height=70,
                        corner_radius=35,  # redondo
                        fg_color=SECONDARY,
                        hover_color=PRIMARY,
                        text_color="white",
                        font=("Helvetica", 20, "bold"))
    btn.place(x=col*80+10, y=row*80+100)

for i, row in enumerate(buttons):
    for j, symbol in enumerate(row):
        create_button(symbol, i, j)

# Ejecutar app
app.mainloop()
