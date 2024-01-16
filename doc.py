import random
from math import log2

# Declarar variables globales
a = 0
b = 0
deltaX = 0
poblacion_maxima = 0

def generar_individuo(n):
    individuo = ''.join(random.choice('01') for _ in range(n))
    return individuo

def operaciones_basicas():
    global a, b, deltaX, poblacion_maxima  # Declarar como globales
    deltaX = float(input("Ingrese el valor de deltaX: "))
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    poblacion_maxima = int(input("Ingrese el valor de la población máxima: "))

    if deltaX <= 0 or a >= b:
        print("Error: Verifique que deltaX sea positivo y que 'a' sea menor que 'b'.")
        exit()

    rango = b - a
    saltos = rango / deltaX
    puntos = saltos + 1
    n = int(log2(puntos))

    while not (2 ** (n - 1) < puntos <= 2 ** n):
        n += 1

    return int(n)

def generar_poblacion():
    n = operaciones_basicas()
    poblacion = []

    for _ in range(poblacion_maxima):
        individuo = generar_individuo(n)
        valor_entero = int(individuo, 2)
        x = a + valor_entero * deltaX  # Calcula el valor de x
        poblacion.append([individuo, valor_entero, x])

    return poblacion

# Ejemplo de uso
poblacion_resultados = generar_poblacion()

# Imprimir la tabla
print("Individuo, Valor Entero, x")
for individuo, valor_entero, x in poblacion_resultados:
    print(f"{individuo}, {valor_entero}, {x}")