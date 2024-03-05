import random
import math

class Annealing:
    def __init__(self, graph, initial_temperature, cooling_rate, max_iterations):
        self.graph = graph
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.max_iterations = max_iterations

  
    def initial_solution(self):
        start_vertex = random.choice(list(self.graph.keys()))
        current_vertex = start_vertex
        visited = {current_vertex}
        path = [current_vertex]

        while len(visited) < len(self.graph):
            neighbors = [neighbor for neighbor in self.graph[current_vertex] if neighbor not in visited]
            if not neighbors:
                start_vertex = random.choice(list(self.graph.keys()))
                current_vertex = start_vertex
                visited = {current_vertex}
                path = [current_vertex]
            else:
                next_vertex = random.choice(neighbors)
                path.append(next_vertex)
                visited.add(next_vertex)
                current_vertex = next_vertex

        if path[-1] not in self.graph[path[0]]:
            return self.initial_solution()
        return path

  
    def calculate_distance(self, path):
        distance = 0
        n = len(path)
        for i in range(n):
            vertex1, vertex2 = path[i], path[(i + 1) % n]
            if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
                distance += self.graph[vertex1][vertex2]
            else:
                return None
        return distance

  
    def simulated_annealing(self):
        current_path = self.initial_solution()
        current_distance = self.calculate_distance(current_path)

        best_path = current_path.copy()
        best_distance = current_distance
        temperature = self.initial_temperature

        for _ in range(self.max_iterations):
            if best_distance is None:
                break

            vertex_indices = list(self.graph.keys())
            i, j = sorted(random.sample(range(len(vertex_indices)), 2))
            vertex1, vertex2 = vertex_indices[i], vertex_indices[j]

            if (current_path[(current_path.index(vertex1) - 1) % len(current_path)] not in self.graph[vertex2]) or \
               (current_path[(current_path.index(vertex1) + 1) % len(current_path)] not in self.graph[vertex2]) or \
               (current_path[(current_path.index(vertex2) - 1) % len(current_path)] not in self.graph[vertex1]) or \
               (current_path[(current_path.index(vertex2) + 1) % len(current_path)] not in self.graph[vertex1]):
                continue
            
            new_path = current_path[:current_path.index(vertex1)] + [vertex2] + current_path[current_path.index(vertex1) + 1:]
            new_path = new_path[:new_path.index(vertex2)] + [vertex1] + new_path[new_path.index(vertex2) + 1:]
            new_distance = self.calculate_distance(new_path)
            if new_distance is None:
                continue
            distance_difference = new_distance - current_distance

            if distance_difference < 0 or random.random() < math.exp(-distance_difference / temperature):
                current_path = new_path
                current_distance = new_distance
                if current_distance < best_distance:
                    best_path = current_path.copy()
                    best_distance = current_distance

            temperature *= self.cooling_rate
        return best_path
