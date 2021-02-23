"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraphUtil(self, node: 'Node', map_gg: dict) -> 'Node':
        if node == None:
            return None
        if node in map_gg:
            return map_gg[node]
        new_node = Node(node.val)
        map_gg[node] = new_node
        for neighbor in node.neighbors:
            new_node.neighbors.append(self.cloneGraphUtil(neighbor, map_gg))
        return new_node
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        map_gg = {}
        print(map_gg)
        return self.cloneGraphUtil(node, map_gg)
