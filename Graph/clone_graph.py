class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {vertex: [] for vertex in vertices}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(graph):
    if not graph:
        return None

    old_to_new = {}

    def dfs(node):
        if node in old_to_new:
            return old_to_new[node]

        clone = Node(node)
        old_to_new[node] = clone

        for neighbor in graph.adj_list[node]:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(list(graph.adj_list.keys())[0])  # Start DFS from any vertex


def dfs_traversal(node):
    visited = set()
    
    def dfs_recursive(vertex):
        if vertex in visited:
            return
        print(vertex.val, end=" ")
        visited.add(vertex)
        for neighbor in vertex.neighbors:
            dfs_recursive(neighbor)

    dfs_recursive(node)


vertices = ["A", "B", "C", "D"]
edges = [("A", "B"), ("B", "D"), ("A", "C"), ("B", "C"), ("C", "D")]

graph = Graph(vertices)

for edge in edges:
    graph.add_edge(*edge)

new_graph = clone_graph(graph)

print("\nCloned graph DFS traversal:")
dfs_traversal(new_graph)
