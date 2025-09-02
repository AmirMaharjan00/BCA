import heapq
class Graph:
    def __init__(self):
        self.graph = {}  # Adjacency list: {node: [(neighbor, cost), ...]}
    
    def add_edge(self, vertex, neighbor, cost):
        """Add an edge with a cost to the graph."""
        if vertex not in self.graph:
            self.graph[vertex] = []
        self.graph[vertex].append((neighbor, cost))
        
        # For undirected graphs, add the reverse edge
        if neighbor not in self.graph:
            self.graph[neighbor] = []
        self.graph[neighbor].append((vertex, cost))

    def uniform_cost_search(self, start, goal):
        """Uniform Cost Search (UCS) implementation."""
        # Priority queue to hold nodes and their cumulative costs
        priority_queue = [(0, start)]  # (cumulative_cost, vertex)
        visited = set()
        
        while priority_queue:
            cost, current = heapq.heappop(priority_queue)  # Pop the node with the lowest cost
            
            if current in visited:
                continue
            
            visited.add(current)
            print(f"Visited Node: {current}, Cost: {cost}")
            
            # Goal test
            if current == goal:
                print(f"Goal Node {goal} reached with Cost: {cost}")
                return
            
            # Expand neighbors
            for neighbor, edge_cost in self.graph.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + edge_cost, neighbor))
        
        print("Goal not reachable!")
        return

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "C", 2)
    g.add_edge("B", "D", 6)
    g.add_edge("C", "D", 3)
    g.add_edge("C", "E", 5)
    g.add_edge("D", "E", 1)
    
    print("Uniform Cost Search from A to E:")
    g.uniform_cost_search("A", "E")