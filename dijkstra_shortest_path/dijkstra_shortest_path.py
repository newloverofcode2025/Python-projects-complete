import heapq

def dijkstra(graph: dict, start: int) -> dict:
    """
    Find the shortest path from a starting node to all other nodes in a weighted graph.
    """
    # Initialize distances to all nodes as infinity, except the start node which is 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to store (distance, node) tuples
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current distance is greater than the recorded distance, skip
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path to the neighbor is found, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

if __name__ == "__main__":
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    start_node = 0
    shortest_paths = dijkstra(graph, start_node)
    print(f"Shortest paths from node {start_node}: {shortest_paths}")