def dfs(graph, v, visited):
    visited.add(v)
    print(v)
    for neighbor in graph.neighbors(v):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def dfs_iter(graph, start):
    visited = set()
    stack = [start]
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        else:
            visited.add(v)
            print(v)
            for neighbor in graph.neighbors(v):
                stack.append(neighbor)


from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque([start])
    while q:  # while len(q) > 0
        v = q.popleft()
        if v in visited:
            continue
        visited.add(v)
        print(v)
        for neighbor in graph.neighbors(v):
            q.append(neighbor)


def has_cycle(graph):
    visited = set()
    for v in graph.vertices:
        if v not in visited and dfs_cycle(
            graph, v, visited, None
        ):
            return True
    return False

def dfs_cycle(graph, v, visited, parent):
    visited.add(v)
    for n in graph.neighbors(v):
        if n not in visited:
            if dfs_cycle(graph, n, visited, v):
                return True
            elif n != parent:
                return True
    return False


def strongly_connected(graph):
    start = next(iter(graph.vertices))
    visited = set()
    dfs(graph, start, visited)
    if len(visited) != len(graph.vertices):
        return False
    reversed_graph = reverse_graph(graph)
    start = next(iter(reversed_graph.vertices))
    visited = set()
    dfs(reversed_graph, start, visited)
    return len(visited) != len(reversed_graph.vertices)

def reverse_graph(graph):
    rev = AdjacencySetGraph()
    for u in graph.adj:
        for v in graph.adj[u]:
            rev.add_edge(v, u)
    return rev


class MatrixGraph:
    def __init__(self, size):
        self.size = size
        self.matrix = [
            [0] * size for _ in range(size)
        ]

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def remove_edge(self, u, v):
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0

    def neighbors(self, v):
        result = []
        for i in range(self.size):
            if self.matrix[v][i] == 1:
                result.append(i)
        return result

        result = []
        for i, x in enumerate(self.matrix[v]):
            if x == 1:
                result.append(i)
        return result

        result = []
        for i, x in enumerate(self.matrix[v]):
            if x:
                result.append(i)
        return result

        return [i for i, x in enumerate(self.matrix[v]) if x]


def connected_components(graph):
    visited = set()
    components = []
    for v in graph.adj:
        if v not in visited:
            component_visited = set()
            dfs(graph, v, component_visited):
            visited.update(component_visited)
            components.append(component_visited)
    return components


