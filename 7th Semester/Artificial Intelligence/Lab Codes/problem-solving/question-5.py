import heapq
class Graph:
    def __init__(self):
        self.graph = {}  # Adjacency list: {node: [(neighbor, cost), ...]}
        self.heuristics = {}  # Heuristic values: {node: heuristic_value}
    
    def add_edge(self, vertex, neighbor, cost):
        """Add an edge with a cost to the graph."""
        if vertex not in self.graph:
            self.graph[vertex] = []
        self.graph[vertex].append((neighbor, cost))
    
    def set_heuristic(self, node, value):
        """Set heuristic value for a node."""
        self.heuristics[node] = value
    
    def greedy_best_first_search(self, start, goal):
        """Greedy Best-First Search implementation."""
        priority_queue = [(self.heuristics[start], start)]  # (heuristic_value, vertex)
        visited = set()
        
        print("Path Traversed:", end=" ")
        
        while priority_queue:
            h_value, current = heapq.heappop(priority_queue)  # Node with smallest heuristic value
            
            if current in visited:
                continue
            
            print(current, end=" -> ")
            visited.add(current)
            
            # Goal test
            if current == goal:
                print("Goal Reached!")
                return
            
            # Explore neighbors
            for neighbor, _ in self.graph.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (self.heuristics[neighbor], neighbor))
        
        print("Goal not reachable!")
        return

# Example usage
if __name__ == "__main__":
    g = Graph()
    # Adding edges to the graph
    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "D", 6)
    g.add_edge("B", "E", 2)
    g.add_edge("C", "F", 5)
    g.add_edge("E", "G", 1)
    g.add_edge("F", "G", 2)
    
    # Setting heuristic values (lower = better)
    g.set_heuristic("A", 7)
    g.set_heuristic("B", 4)
    g.set_heuristic("C", 6)
    g.set_heuristic("D", 8)
    g.set_heuristic("E", 2)
    g.set_heuristic("F", 3)
    g.set_heuristic("G", 0)
    
    print("Greedy Best-First Search from A to G:")
    g.greedy_best_first_search("A", "G")