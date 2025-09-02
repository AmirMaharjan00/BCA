class Graph:
    def __init__(self):
        self.graph = {}  # Adjacency list representation
    
    def add_edge(self, vertex, neighbor):
        """Add an edge to the graph."""
        if vertex not in self.graph:
            self.graph[vertex] = []
        self.graph[vertex].append(neighbor)
    
    def dfs(self, start, visited=None):
        """Recursive implementation of Depth First Search."""
        if visited is None:
            visited = set()
        
        visited.add(start)
        print(start, end=" ")  # Print the current vertex
        
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)
    
    def dfs_iterative(self, start):
        """Iterative implementation of Depth First Search."""
        visited = set()
        stack = [start]
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                # Add neighbors to the stack (in reverse order for correct traversal)
                stack.extend(reversed(self.graph.get(vertex, [])))

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    
    print("DFS (Recursive):")
    g.dfs(0)
    print("\nDFS (Iterative):")
    g.dfs_iterative(0)