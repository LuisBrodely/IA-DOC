import random
from math import log2

def generar_individuo(n):
    individuo = ''.join(random.choice('01') for _ in range(n))
    return individuo

def operaciones_basicas():
    deltaX = float(input("Ingrese el valor de deltaX: "))
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))

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
    poblacion_maxima = int(input("Ingrese el valor de la población máxima: "))
    n = operaciones_basicas()
    poblacion = []

    for _ in range(poblacion_maxima):
        individuo = generar_individuo(n)
        valor_entero = int(individuo, 2)
        poblacion.append([individuo, valor_entero])

    return poblacion

# Ejemplo de uso
poblacion_resultados = generar_poblacion()

# Imprimir la tabla
print("Individuo, Valor Entero")
for individuo, individuo_entero in poblacion_resultados:
    print(f"{individuo}, {individuo_entero}")
