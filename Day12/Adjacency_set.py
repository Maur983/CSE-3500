class graph:
    def __init__(self):
        self.adj = dict()
    
    def add_vertex(self,v):
        if v not in self.adj:
            self.adj[v] = set()
    
    def add_edges(self, u,v):
        self.add_vertex(v)
        self.add_vertex(u)
        self.adj[v].add(u)
        self.adj[u].add(v)
    
    def remove_edges(self,u,v):
        if u in self.adj:
            self.adj[u].dicard(v)
        
        if v in self.adj:
            self.adj[v].dicard(u)
    
    def remove_vertex(self,v):
        if v not in self.adj:
            return
        
        for neighbor in self.adj[v]:
            self.adj[neighbor].discard(v)
        
        del self.adj[v]

    def neighbors(self,v):
        return self.adj.get(v, set())