
# Task 2: Self-Study on Graph and BFS
# Data Structure: Graph (Adjacency List)
# Algorithm: Breadth-First Search (BFS)

class Campus:
    def __init__(self):
        # The Abstract Data Type (ADT) is implemented using a dictionary
        # where keys are nodes and values are lists of connected neighbors.
        self.adj_list = {}

    def add_edge(self, u, v):
        """Adds an undirected connection between node u and node v."""
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []

        # Adding edges for both directions (undirected graph)
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start_node):
        """Algorithm to traverse the graph layer by layer."""
        visited = []          # Keeps track of nodes that already exist
        queue = [start_node]  # Queue controls the order of exploration (First-In-First-Out)

        visited.append(start_node)
        print(f"--- Starting BFS from: {start_node} ---")

        while queue:
            # Remove the first element from the queue
            current_node = queue.pop(0)
            print(f"Visited: {current_node}")

            # Explore all neighbors of the current node
            for neighbor in self.adj_list.get(current_node, []):
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor) # Add to the back of the queue

        return visited

# --- Demonstration for Task 2 ---
if __name__ == "__main__":
    # 1. Create a name that represent campus map and calls the function
    campus_map = Campus()

    # 2. Add edges (paths between campus buildings)
    campus_map.add_edge("Main Gate", "Library")
    campus_map.add_edge("Main Gate", "Cafeteria")
    campus_map.add_edge("Library", "Block A")
    campus_map.add_edge("Cafeteria", "Block A")
    campus_map.add_edge("Block A", "Science Labs")

    # 3. Run the Breadth-First Search Algorithm
    campus_map.bfs("Main Gate")
