import random
import string

# Definir la cadena objetivo que queremos encontrar
objetivo = "hola, mundo!"

# Definir una función para generar una cadena aleatoria de caracteres
def generar_cadena(longitud):
    return ''.join(random.choice(string.ascii_lowercase + ' ,.!?') for _ in range(longitud))

# Definir una función de aptitud que mida cuántos caracteres coinciden con el objetivo
def aptitud(cadena):
    return sum(1 for a, b in zip(cadena, objetivo) if a == b)

# Definir una función de reproducción que crea una nueva cadena combinando dos padres
def reproducir(padre1, padre2):
    punto_corte = random.randint(1, len(padre1) - 1)
    hijo = padre1[:punto_corte] + padre2[punto_corte:]
    return hijo

# Definir una función de mutación que cambia un carácter al azar en la cadena
def mutar(cadena, tasa_mutacion):
    if random.random() < tasa_mutacion:
        indice = random.randint(0, len(cadena) - 1)
        cadena = cadena[:indice] + random.choice(string.ascii_lowercase + ' ,.!') + cadena[indice + 1:]
    return cadena

# Parámetros del algoritmo
tamano_poblacion = 100
tasa_mutacion = 0.1
generaciones_maximas = 10000

# Crear una población inicial de cadenas aleatorias
poblacion = [generar_cadena(len(objetivo)) for _ in range(tamano_poblacion)]

for generacion in range(generaciones_maximas):
    # Calcular la aptitud de cada cadena en la población
    puntuaciones = [aptitud(cadena) for cadena in poblacion]

    # Verificar si alguna cadena coincide completamente con el objetivo
    mejor_aptitud = max(puntuaciones)
    mejor_cadena = poblacion[puntuaciones.index(mejor_aptitud)]

    if mejor_aptitud == len(objetivo):
        print(f"Generación {generacion}: {mejor_cadena}")
        break

    # Seleccionar dos padres con probabilidades ponderadas por la aptitud
    padres = random.choices(poblacion, weights=puntuaciones, k=2)

    # Crear un hijo mediante reproducción
    hijo = reproducir(padres[0], padres[1])

    # Aplicar mutación al hijo
    hijo = mutar(hijo, tasa_mutacion)

    # Reemplazar a un miembro aleatorio de la población si el hijo es mejor
    if aptitud(hijo) > min(puntuaciones):
        poblacion[random.choices(range(tamano_poblacion), k=1)[0]] = hijo

# Imprimir la cadena encontrada o el mensaje de que no se encontró
print(f'{mejor_cadena=}')
print("Cadena encontrada:", mejor_cadena if mejor_aptitud == len(objetivo) else "No se encontró una coincidencia.")
