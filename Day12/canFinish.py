class Solution:
    def canFinish(self, numCourses, prerequisites):
        finished = set()
        visited = set()
        neighbors = {}
        for i in prerequisites:
            if i[0] in neighbors:
                neighbors[i[0]].append(i[1])
            else:
                neighbors[i[0]] = [i[1]]

        def dfs(node):
            if node in finished:
                return True

            if node in visited:
                return False
            visited.add(node)
            for next_node in neighbors.get(node, []):
                if not dfs(next_node):
                    return False
            finished.add(node)
            visited.remove(node)
            return True
        for i in range(numCourses):
            if i not in finished and not dfs(i):
                return False
        return True
        