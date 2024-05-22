import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.vertices:
            self.vertices[from_vertex] = []
        if to_vertex not in self.vertices:
            self.vertices[to_vertex] = []
        self.vertices[from_vertex].append((to_vertex, weight))
        self.vertices[to_vertex].append((from_vertex, weight))  

    def __str__(self):
        return str(self.vertices)


def dijkstra(graph, start_vertex):

    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        

        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph.vertices[current_vertex]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances


def main():
    graph = Graph()
    edges = [
        ('A', 'B', 1),
        ('A', 'C', 4),
        ('B', 'C', 2),
        ('B', 'D', 5),
        ('C', 'D', 1),
        ('D', 'E', 3)
    ]
    
    for edge in edges:
        graph.add_edge(*edge)
    
    print("Граф:", graph)
    
    start_vertex = 'A'
    shortest_paths = dijkstra(graph, start_vertex)
    
    print(f"Найкоротші шляхи від вершини {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"Вершина {vertex}: відстань {distance}")

if __name__ == "__main__":
    main()

