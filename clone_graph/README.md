## Clone Graph

### Description
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
Note: Each node's value is the same as the node's index (1-indexed). For simplicity, each node's value is the same as the node's index (1-indexed).
Input:
Node 1's value is 1, and it has two neighbors with values 2 and 4.
Node 2's value is 2, and it has one neighbor with value 4.
Node 3's value is 3, and it has one neighbor with value 2.
Node 4's value is 4, and it has two neighbors with values 1 and 3.
Output:
A deep copy of the graph.

A function to return a deep copy of the graph.

### File
- [clone_graph.py](clone_graph.py)
Run the code in VS Code by pressing F5 or by clicking the "Run" button in the top-right corner.
Verify the output:
Original Graph:
Node 1 -> Neighbors: [2, 4]
Node 2 -> Neighbors: [1, 3]
Node 3 -> Neighbors: [2, 4]
Node 4 -> Neighbors: [1, 3]

Cloned Graph:
Node 1 -> Neighbors: [2, 4]
Node 2 -> Neighbors: [1, 3]
Node 3 -> Neighbors: [2, 4]
Node 4 -> Neighbors: [1, 3]
