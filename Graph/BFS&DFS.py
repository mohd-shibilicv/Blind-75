from collections import deque


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {vertex: [] for vertex in vertices}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)


def bfs(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            for neighbor in graph.adj_list[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)


def dfs(graph, start_vertex):
    visited = set()

    def dfs_recursive(vertex):
        print(vertex, end=" ")
        visited.add(vertex)
        for neighbor in graph.adj_list[vertex]:
            if neighbor not in visited:
                dfs_recursive(neighbor)

    dfs_recursive(start_vertex)


vertices = ['A', 'B', 'C', 'D']
edges = [('A', 'B'), ('B', 'D'), ('A', 'C'), ('B', 'C'), ('C', 'D')]

graph = Graph(vertices)

for edge in edges:
    graph.add_edge(*edge)

bfs(graph, 'A')
print()
dfs(graph, 'A')
