import numpy as np

# Graph Combinations
# Анна connected: Богдан, Віктор, Ганна
# Богдан connected: Анна, Віктор, Дмитро
# Віктор connected: Анна, Богдан, Ганна, Дмитро
# Ганна connected: Анна, Віктор, Євген
# Дмитро connected: Богдан, Віктор, Євген
# Євген connected: Ганна, Дмитро

# Анна, Богдан, Віктор, Ганна, Дмитро, Євген
# Анна    0  1  1  1  0  0
# Богдан  1  0  1  0  1  0
# Віктор  1  1  0  1  1  0
# Ганна   1  0  1  0  0  1
# Дмитро  0  1  1  0  0  1
# Євген   0  0  0  1  1  0

# Graph matrix
graph_A = np.array([
    [0, 1, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0]
])

# Dictionary of connection
graph_dict = {
    "Анна": ["Богдан", "Віктор", "Ганна"],
    "Богдан": ["Анна", "Віктор", "Дмитро"],
    "Віктор": ["Анна", "Богдан", "Ганна", "Дмитро"],
    "Ганна": ["Анна", "Віктор", "Євген"],
    "Дмитро": ["Богдан", "Віктор", "Євген"],
    "Євген": ["Ганна", "Дмитро"]
}

# Edges list
graph_edge = [
    ("Анна", "Богдан"),
    ("Анна", "Віктор"),
    ("Анна", "Ганна"),
    ("Богдан", "Віктор"),
    ("Богдан", "Дмитро"),
    ("Віктор", "Ганна"),
    ("Віктор", "Дмитро"),
    ("Ганна", "Євген"),
    ("Дмитро", "Євген")
]

# Vertices degree
graph_deg = {}
for vertex, neighbors in graph_dict.items():
    degree = len(neighbors)
    graph_deg[vertex] = degree
    print(f"{vertex} has degree {degree}")

# Find the vertex with the maximum degree
max_degree_vertex = max(graph_deg, key=graph_deg.get)
print(f"\nVertex with the maximum degree: {max_degree_vertex} ({graph_deg[max_degree_vertex]})")

# Thorem check
edges_count = len(graph_edge)
graph_degrees_sum = sum(graph_deg.values())
print(f"\nNumber of edges: {edges_count}")
print(f"Sum of all vertex degrees: {graph_degrees_sum}")
print(f"Verification (2 * number of edges): {2 * edges_count}")
print(f"Verification passed: {graph_degrees_sum == 2 * edges_count}")
