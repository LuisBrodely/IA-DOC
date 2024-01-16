import random
from math import log2
import tkinter as tk
from tkinter import ttk

# Declarar variables globales
a = 0
b = 0
deltaX = 0
poblacion_maxima = 0

def generar_individuo(n):
    individuo = ''.join(random.choice('01') for _ in range(n))
    return individuo

def obtener_valores():
    global a, b, deltaX, poblacion_maxima
    a = float(entry_a.get())
    b = float(entry_b.get())
    deltaX = float(entry_deltaX.get())
    poblacion_maxima = int(entry_poblacion_maxima.get())

    if deltaX <= 0 or a >= b:
        error_label.config(text="Error: Verifique que deltaX sea positivo y que 'a' sea menor que 'b'.")
        return

    error_label.config(text="")
    root.destroy()  # Cerrar la ventana después de obtener los valores

def generar_poblacion():
    n = int(log2((b - a) / deltaX) + 1)
    poblacion = []

    for _ in range(poblacion_maxima):
        individuo = generar_individuo(n)
        valor_entero = int(individuo, 2)
        x = a + valor_entero * deltaX
        poblacion.append([individuo, valor_entero, x])

    return poblacion

# Interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Configuración de Parámetros")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Labels y Entry para los valores
ttk.Label(frame, text="DeltaX:").grid(row=0, column=0, sticky=tk.W)
entry_deltaX = ttk.Entry(frame)
entry_deltaX.grid(row=0, column=1)

ttk.Label(frame, text="a:").grid(row=1, column=0, sticky=tk.W)
entry_a = ttk.Entry(frame)
entry_a.grid(row=1, column=1)

ttk.Label(frame, text="b:").grid(row=2, column=0, sticky=tk.W)
entry_b = ttk.Entry(frame)
entry_b.grid(row=2, column=1)

ttk.Label(frame, text="Población máxima:").grid(row=3, column=0, sticky=tk.W)
entry_poblacion_maxima = ttk.Entry(frame)
entry_poblacion_maxima.grid(row=3, column=1)

error_label = ttk.Label(frame, text="", foreground="red")
error_label.grid(row=4, column=0, columnspan=2, pady=(10, 0))

# Botón para obtener valores
ttk.Button(frame, text="Aceptar", command=obtener_valores).grid(row=5, column=0, columnspan=2, pady=(10, 0))

root.mainloop()

# Generar población después de obtener valores
poblacion_resultados = generar_poblacion()

# Imprimir la tabla
print("Individuo, Valor Entero, x")
for individuo, valor_entero, x in poblacion_resultados:
    print(f"{individuo}, {valor_entero}, {x}")
