import heapq
import time

class AnytimeAStar:
    def __init__(self, graph):
        self.graph = graph

    def shortest_path(self, start, goal, time_limit):
        open_set = []
        heapq.heappush(open_set, (0, start))
        g_score = {node: float('inf') for node in self.graph}
        g_score[start] = 0
        came_from = {}  # Corrección: Utilizar un diccionario para almacenar nodos padres
        current_best_path = []

        start_time = time.time()

        while open_set and (time.time() - start_time) < time_limit:
            current_cost, current_node = heapq.heappop(open_set)

            if current_node == goal:
                current_best_path = self.reconstruct_path(goal, start, came_from)
                continue

            for neighbor, cost in self.graph[current_node].items():
                tentative_g_score = g_score[current_node] + cost

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current_node  # Actualizar el nodo padre
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))

        return current_best_path

    def heuristic(self, node, goal):
        x1, y1 = node
        x2, y2 = goal
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def reconstruct_path(self, current, start, came_from):
        path = [current]
        while current != start:
            current = came_from[current]
            path.append(current)
        return path[::-1]

# Ejemplo de uso (sin cambios)
graph = {
    (0, 0): {(1, 0): 1, (0, 1): 2},
    (1, 0): {(0, 0): 1, (1, 1): 1, (2, 0): 2},
    (2, 0): {(1, 0): 2, (2, 1): 1},
    (0, 1): {(0, 0): 2, (0, 2): 1, (1, 1): 2},
    (1, 1): {(1, 0): 1, (0, 1): 2, (2, 1): 1},
    (2, 1): {(2, 0): 1, (1, 1): 1, (2, 2): 2},
    (0, 2): {(0, 1): 1, (1, 2): 2},
    (1, 2): {(0, 2): 2, (1, 1): 2, (2, 2): 1},
    (2, 2): {(1, 2): 1, (2, 1): 2}
}

astar = AnytimeAStar(graph)
start_node = (0, 0)
goal_node = (2, 2)
time_limit = 1.0

best_path = astar.shortest_path(start_node, goal_node, time_limit)
print("Mejor camino encontrado hasta ahora:", best_path)

