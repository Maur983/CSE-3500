class Solution:
    def allPathsSourceTarget(self, graph):
        numnodes = len(graph)
        path = []
        reslist = []

        def dfs(node):
            path.append(node)                
            if path[-1] == numnodes-1:
                reslist.append(path[:])
            for neigh in graph[node]:
                dfs(neigh)
            path.pop()
        
        dfs(0)
        return reslist