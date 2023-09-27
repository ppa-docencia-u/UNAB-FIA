import math
import random

# Función para calcular la distancia euclidiana entre dos puntos (ciudades)
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Función para calcular la longitud total de una ruta (orden de visitas)
def total_distance(route, cities):
    total = 0
    for i in range(len(route) - 1):
        total += distance(cities[route[i]], cities[route[i + 1]])
    return total

# Algoritmo Simulated Annealing
def simulated_annealing(cities, initial_temperature, cooling_rate, max_iterations):
    num_cities = len(cities)
    current_route = list(range(num_cities))
    random.shuffle(current_route)  # Generar una solución inicial aleatoria
    current_distance = total_distance(current_route, cities)

    best_route = current_route.copy()
    best_distance = current_distance

    for iteration in range(max_iterations):
        temperature = initial_temperature * (1 - iteration / max_iterations)
        if temperature <= 0.01:
            break

        # Generar una nueva solución vecina intercambiando dos ciudades
        neighbor_route = current_route.copy()
        i, j = random.sample(range(num_cities), 2)
        neighbor_route[i], neighbor_route[j] = neighbor_route[j], neighbor_route[i]
        neighbor_distance = total_distance(neighbor_route, cities)

        # Calcular la diferencia de distancias entre la nueva solución y la actual
        delta_distance = neighbor_distance - current_distance

        # Si la nueva solución es mejor o se acepta según la probabilidad de Boltzmann
        if delta_distance < 0 or random.random() < math.exp(-delta_distance / temperature):
            current_route = neighbor_route
            current_distance = neighbor_distance

            # Actualizar la mejor solución si es necesario
            if current_distance < best_distance:
                best_route = current_route.copy()
                best_distance = current_distance

    return best_route, best_distance

# Generar un conjunto de ciudades aleatorias (coordenadas x, y)
random.seed(42)
num_cities = 10
cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_cities)]

# Parámetros del algoritmo
initial_temperature = 1000.0
cooling_rate = 0.995
max_iterations = 10000

# Ejecutar Simulated Annealing
best_route, best_distance = simulated_annealing(cities, initial_temperature, cooling_rate, max_iterations)

# Mostrar la mejor ruta y su longitud
print("Mejor ruta encontrada:", best_route)
print("Longitud de la mejor ruta:", best_distance)
