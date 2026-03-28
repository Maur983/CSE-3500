#We use set.dicard in this is because if the element is not in the set then it won't cause an error
#When working with graphs often we code the graphs.
from collections import deque
import itertools
class EdgeSetGraph:
    def __init__(self): #Time O(1) Space O(1)
        self.vertices = set()
        self.edges = set()

    def add_vertex(self,v): #Time O(1)
        self.vertices.add(v)
    
    def add_edge(self,u,v): #Time O(1)
        self.vertices.add(u)
        self.vertices.add(v)
        self.edges.add(frozenset({u,v})) #Frozen set is a imutable set so that it can be hashed since we can't normally put a set in set and this is good here this is a simple graph.

    def remove_edge(self,u,v): #Time O(1)
        self.edges.discard(frozenset({u,v}))
    
    def remove_vertex(self,v): # Time O(e) which are the amount of edges
        self.vertices.discard(v)
        #self.edges = {e for e in self.edges if v not in e}
        temp = {}
        for e in self.edges:
            if v not in e:
                temp.add(e)
        self.edges = temp
    
    def neighbors(self, v): #Time O(e) all of the edges
        result = set()
        for u ,w in self.edges:
            if u ==v:
                result.add(w)
            elif w==v:
                result.add(u)
        return result
    
class AdjacencySetGraph: #This is the superior graph and should be used. Space O(e) which is all of the edges this is a undrected graph
    def __init__(self):
        self.adj = dict()

    def add_vertex(self,v): #Time O(1)
        if v not in self.adj:
            self.adj[v] = set()
    
    def add_edge(self, u,v): #Time O(1)
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].add(v)
        self.adj[v].add(u)

    def remove_edge(self,u,v): #Time O(1)
        if u in self.adj:
            self.adj[u].discard(v)
        if v in self.adj:
            self.adj[v].discard(u)

    def remove_vertex(self,v): #Time O(n) or number of neighbors
        if v not in self.adj:
            return
        for neighbor in self.adj[v]:
            self.adj[neighbor].discard(v)
        del self.adj[v]

    def neighbors(self,v): #Time O(1)
        return self.adj.get(v, set())
    
def dfs(graph, v , visited):
    visited.add(v)
    print(v)
    for neighbor in graph.neighbors(v):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def dfs_iter(graph, start):
    visited = set()
    stack =[start]
    while stack:
        v = stack.pop()
        if v in visited:
            continue #Continue will skip to next part of the stack
        else:
            visited.add(v)
            print(v)
            for neighbor in graph.neighbors(v):
                stack.append(neighbor)

def bfs(graph, start):
    visited = set()
    q = deque([start])
    while q: #while len(queue)>0
        v = q.popleft()
        if v in visited:
            continue
        visited.add(v)
        print(v)
        for neighbor in graph.neighbors(v):
            q.append(neighbor)

def dfs_cycle(graph, v, visited , parent):
    visited = set()
    for n in graph.neighbors(v):
        if n not in visited:
            if dfs_cycle(graph,n,visited, v):
                return True
            elif n!=parent:
                return True
    return False

def has_cycle(graph):
    visited = set()
    for v in graph.vertices:
        if v not in visited and dfs_cycle(graph,v,visited,None):
            return True
    return False

def strongly_connectivity(graph):
    start = next(iter(graph.vertices)) #This how find the first value of any set or hashmap
    visited  = set()
    dfs(graph, start, visited)
    if len(visited) != len(graph.vertices):
        return False
    reversed_graph = reverse_graph(graph)
    start = next(iter(graph.vertices))
    visited = set ()
    dfs(reversed_graph , start , visited )
    return len(visited) == len(graph.vertices)

def reverse_graph(graph):
    rev = AdjacencySetGraph()
    for u in graph.adj:
        for v in graph.adj[u]:
            rev.add_edge(v,u)
    return rev

class MatrixGraph:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0]* size for _ in range(size)]

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def remove_edge(self,u,v):
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0
    
    def neighbors(self,v):
        result = []
        for i,x in enumerate(self.matrix[v]):
            if x ==1:
                result.append(i)
        return result
    
def connected_components(graph):
    visited = set()
    components = []
    for v in graph.adj:
        if v not in visited:
            component_visited = set()
            dfs(graph, v , component_visited)
            visited.update(component_visited)
            components.append(component_visited)
    return components