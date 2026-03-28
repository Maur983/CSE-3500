
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        graph_dict = {node: Node(node.val)}
        queue = deque([node])
        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in graph_dict:
                    graph_dict[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                graph_dict[current].neighbors.append(graph_dict.get(neighbor))
        return graph_dict[node]