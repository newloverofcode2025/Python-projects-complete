class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> 'Node':
    """
    Return a deep copy of the graph.
    """
    if not node:
        return None

    # Dictionary to store the cloned nodes
    cloned_nodes = {}

    def dfs(original):
        if original in cloned_nodes:
            return cloned_nodes[original]

        # Create a new node with the same value
        clone = Node(original.val)
        cloned_nodes[original] = clone

        # Recursively clone the neighbors
        for neighbor in original.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)

# Helper function to print the graph
def print_graph(node):
    visited = set()
    def dfs_print(n):
        if n in visited:
            return
        visited.add(n)
        print(f"Node {n.val} -> Neighbors: {[neighbor.val for neighbor in n.neighbors]}")
        for neighbor in n.neighbors:
            dfs_print(neighbor)
    dfs_print(node)

if __name__ == "__main__":
    # Create a sample graph
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    cloned_node = cloneGraph(node1)
    print("Original Graph:")
    print_graph(node1)
    print("\nCloned Graph:")
    print_graph(cloned_node)