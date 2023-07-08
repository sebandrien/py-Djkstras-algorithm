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

# User input for starting and ending vertex
start_vertex = input("Enter the starting vertex: ")
end_vertex = input("Enter the ending vertex: ")

distances, paths = calculate_distances(graph_a, start_vertex)

# Check if the ending vertex is in the distances dictionary
if end_vertex in distances:
    print("Shortest distance from {} to {}: {}".format(start_vertex, end_vertex, distances[end_vertex]))
    print("Path:", paths[end_vertex])
else:
    print("Path does not exist from {} to {}.".format(start_vertex, end_vertex))
