class graph:
    def __init__(self):
        self.vertices = set()
        self.edges = set()

    def add_vertex(self, v):
        self.vertices.add(v)
    
    def add_edges(self, u,v):
        self.vertices.add(u)
        self.vertices.add(v)
        self.edges.add(frozenset({u,v}))
    
    def remove_edges(self, u,v):
        self.edges.discard(frozenset({u,v}))
    
    def remove_vertex(self, v):
        self.vertices.discard(v)
        temp = set()
        for e in self.edges:
            if v not in self.edges:
                temp.add(e)
        self.edges=temp
    
    def neighbors(self, v):
        result = set()
        for e,s in self.edges:
            if e ==v:
                result.add(e)
            elif s==v:
                result.add(s)
        return result
            