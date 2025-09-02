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

    def a_star_search(self, start, goal):
        """A* Search implementation."""
        # Priority queue to hold nodes and their f(n) = g(n) + h(n)
        open_list = [(0 + self.heuristics[start], 0, start)]  # (f(n), g(n), node)
        g_costs = {start: 0}  # Dictionary to track g(n) values
        came_from = {}  # To reconstruct the path
        visited = set()
        
        print("Path Traversed:", end=" ")

        while open_list:
            _, g, current = heapq.heappop(open_list)  # Get the node with lowest f(n)
            
            if current in visited:
                continue

            print(current, end=" -> ")
            visited.add(current)

            # Goal test
            if current == goal:
                print("Goal Reached!")
                self.reconstruct_path(came_from, goal)
                return

            # Explore neighbors
            for neighbor, cost in self.graph.get(current, []):
                tentative_g = g + cost
                if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g
                    f = tentative_g + self.heuristics.get(neighbor, float('inf'))
                    heapq.heappush(open_list, (f, tentative_g, neighbor))
                    came_from[neighbor] = current

        print("Goal not reachable!")
        return
    
    def reconstruct_path(self, came_from, goal):
        """Reconstruct and print the path from start to goal."""
        path = []
        current = goal
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.append(current)
        path.reverse()
        print(" -> ".join(path))

# Example usage
if __name__ == "__main__":
    g = Graph()
    
    # Adding edges (graph structure)
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
    
    print("A* Search from A to G:")
    g.a_star_search("A", "G")