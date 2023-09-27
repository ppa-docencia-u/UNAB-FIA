import random

# Tamaño del entorno bidimensional
tamaño_entorno = (10, 10)

# Posición inicial del agente
posicion_inicial = (0, 0)

# Posición del tesoro (objetivo)
posicion_tesoro = (random.randint(0, tamaño_entorno[0] - 1), random.randint(0, tamaño_entorno[1] - 1))

# Función para calcular la distancia entre dos puntos
def calcular_distancia(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    return abs(x1 - x2) + abs(y1 - y2)

# Función del agente de búsqueda en línea
def buscar_tesoro(posicion_actual, posicion_tesoro):
    while posicion_actual != posicion_tesoro:
        # Determinar la dirección hacia la que moverse
        if posicion_actual[0] < posicion_tesoro[0]:
            movimiento_x = 1
        elif posicion_actual[0] > posicion_tesoro[0]:
            movimiento_x = -1
        else:
            movimiento_x = 0

        if posicion_actual[1] < posicion_tesoro[1]:
            movimiento_y = 1
        elif posicion_actual[1] > posicion_tesoro[1]:
            movimiento_y = -1
        else:
            movimiento_y = 0

        # Actualizar la posición del agente
        posicion_actual = (
            posicion_actual[0] + movimiento_x,
            posicion_actual[1] + movimiento_y
        )

        # Calcular la distancia al tesoro
        distancia = calcular_distancia(posicion_actual, posicion_tesoro)

        # Informar la posición actual y la distancia al tesoro
        print(f"Posición actual: {posicion_actual}, Distancia al tesoro: {distancia}")

    print("¡Tesoro encontrado!")

# Ejecutar la búsqueda del tesoro
print("Posición inicial:", posicion_inicial)
print("Posición del tesoro:", posicion_tesoro)
buscar_tesoro(posicion_inicial, posicion_tesoro)
