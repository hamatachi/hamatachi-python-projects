
import heapq

def simplified_dijkstra(graph, start):
    queue = [(0, start)]  # priority queue with (distance, node)
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                
    return distances

# Example graph represented as an adjacency list
graph = {
    'London': {'Paris': 10, 'Shanghai': 40},
    'Paris': {'London': 10, 'Shanghai': 30, 'Tokyo': 70},
    'Shanghai': {'London': 40, 'Paris': 30, 'Tokyo': 10},
    'Tokyo': {'Paris': 70, 'Shanghai': 10}
}

# Run the simplified Dijkstra's algorithm
start_node = 'London'
shortest_paths = simplified_dijkstra(graph, start_node)

# Print the shortest paths
for node, distance in shortest_paths.items():
    print(f"Distance from {start_node} to {node} is {distance} ms")
    
