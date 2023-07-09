import heapq

def calculate_distances(graph, starting_vertex, target_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    paths = {vertex: [] for vertex in graph}
    paths[starting_vertex] = [starting_vertex]

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_vertex] + [neighbor]
                heapq.heappush(pq, (distance, neighbor))

    return distances[target_vertex], paths[target_vertex]

graph_a = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 1},
    'D': {'B': 1, 'C': 1},
}

graph_b = {
    'A': {'B': 1, 'C': 3, 'E': 6},
    'B': {'A': 1, 'C': 2, 'D': 1, 'F': 7},
    'C': {'A': 3, 'B': 2, 'D': 1, 'E': 1, 'G': 8},
    'D': {'B': 1, 'C': 1},
    'E': {'A': 6, 'C': 1},
    'F': {'B': 7},
    'G': {'C': 8},
}

start_vertex = 'A'
end_vertex = 'D'
distance, path = calculate_distances(graph_a, start_vertex, end_vertex)
print(f"Pathed from: {start_vertex} to {end_vertex}")
print("Shortest distance to target:", distance)
print("Shortest path to target:", ' -> '.join(path))

print("\n")

start_vertex = 'A'
end_vertex = 'G'
distance, path = calculate_distances(graph_b, start_vertex, end_vertex)
print(f"Pathed from: {start_vertex} to: {end_vertex}")
print("Shortest distance to target:", distance)
print("Shortest path to target:", ' -> '.join(path))
