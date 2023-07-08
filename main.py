import heapq # Importing the heapq module for Priority Queue

def calculate_distances(graph, starting_vertex):
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

    return distances, paths

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
    'D': {'B': 1, 'C': 1, 'H': 9},
    'E': {'A': 6, 'C': 1, 'I': 10},
    'F': {'B': 7, 'J': 11},
    'G': {'C': 8, 'K': 12},
    'H': {'D': 9},
    'I': {'E': 10},
    'J': {'F': 11},
    'K': {'G': 12},
}

distances, paths = calculate_distances(graph_a, 'A')
print("Shortest distances:", distances)

farthest_node = max(distances, key=distances.get) # Find the farthest node
print("Farthest node:", farthest_node)

print("Shortest path from starting node to farthest node:", paths[farthest_node]) 

distances, paths = calculate_distances(graph_b, 'A')
print("Shortest distances:", distances)

farthest_node = max(distances, key=distances.get) # Find the farthest node
print("Farthest node:", farthest_node)

print("Shortest path from starting node to farthest node:", paths[farthest_node]) # Get the shortest path to the farthest node
