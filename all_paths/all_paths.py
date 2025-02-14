def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    """
    Find all paths from the start node to the target node in a directed graph.
    """
    def dfs(node, path):
        if node == len(graph) - 1:  # If we reached the target node
            result.append(path[:])
            return
        for neighbor in graph[node]:
            path.append(neighbor)
            dfs(neighbor, path)
            path.pop()

    result = []
    dfs(0, [0])  # Start from the source node
    return result

if __name__ == "__main__":
    graph = [
        [1, 2],  # Node 0
        [3],     # Node 1
        [3],     # Node 2
        []       # Node 3
    ]
    start_node = 0
    target_node = len(graph) - 1
    paths = allPathsSourceTarget(graph)
    print(f"All paths from node {start_node} to node {target_node}: {paths}")
    