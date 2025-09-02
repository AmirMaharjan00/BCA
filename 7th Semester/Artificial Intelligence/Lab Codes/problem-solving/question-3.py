from collections import deque
class Graph:
    def __init__(self):
        self.graph = {}  # Adjacency list representation
    
    def add_edge(self, vertex, neighbor):
        """Add an edge to the graph."""
        if vertex not in self.graph:
            self.graph[vertex] = []
        self.graph[vertex].append(neighbor)
    
    def bfs(self, start):
        """Implementation of Breadth-First Search."""
        visited = set()  # To track visited nodes
        queue = deque([start])  # Queue for BFS (FIFO)
        print("BFS Traversal:", end=" ")
        
        while queue:
            vertex = queue.popleft()  # Dequeue the front of the queue
            
            if vertex not in visited:
                print(vertex, end=" ")  # Process the current node
                visited.add(vertex)
                
                # Enqueue all unvisited neighbors
                for neighbor in self.graph.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    print( "Graph: ", g.graph )
    g.bfs(0)