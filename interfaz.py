
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

ventana = tk.Tk()
ventana.title("Sistema de Inventario")
ventana.geometry("500x420")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana,
    text="SISTEMA DE INVENTARIO",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=20)

subtitulo = tk.Label(
    ventana,
    text="Proyecto Final de Algoritmos",
    font=("Arial", 11)
)
subtitulo.pack(pady=5)


def abrir_programa():
    try:
        subprocess.Popen([sys.executable, "main.py"])
    except Exception as error:
        messagebox.showerror("Error", str(error))


def mostrar_info():
    messagebox.showinfo(
        "Funciones del sistema",
        "El sistema incluye:\n"
        "- Productos\n"
        "- Clientes\n"
        "- Pedidos\n"
        "- Reportes\n"
        "- Cotizaciones por correo\n"
        "- Copias de seguridad"
    )


tk.Button(
    ventana,
    text="Abrir sistema de consola",
    width=30,
    command=abrir_programa
).pack(pady=15)

tk.Button(
    ventana,
    text="Ver funciones del sistema",
    width=30,
    command=mostrar_info
).pack(pady=10)

tk.Button(
    ventana,
    text="Salir",
    width=30,
    command=ventana.destroy
).pack(pady=10)

ventana.mainloop()
