import random
import math

# Función objetivo
def objective_function(x):
    return math.sin(x) * (x ** 2)

# Algoritmo Hill Climbing
def hill_climbing(max_iterations, step_size):
    current_solution = random.uniform(0, 2 * math.pi)  # Generamos una solución inicial aleatoria
    current_value = objective_function(current_solution)

    for _ in range(max_iterations):
        next_solution = current_solution + random.uniform(-step_size, step_size)
        next_value = objective_function(next_solution)

        if next_value > current_value:
            current_solution = next_solution
            current_value = next_value

    return current_solution, current_value

# Parámetros del algoritmo
max_iterations = 1000
step_size = 0.1

# Ejecutar Hill Climbing
best_solution, best_value = hill_climbing(max_iterations, step_size)

# Mostrar resultados
print("Mejor solución encontrada:", best_solution)
print("Valor de la función objetivo en la mejor solución:", best_value)
