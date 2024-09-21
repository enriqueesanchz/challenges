from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        nodes = {}
        def clone(node):
            if node.val in nodes:
                return nodes[node.val]
            
            nnode = Node(node.val)
            nodes[nnode.val] = nnode

            for n in node.neighbors:
                nnode.neighbors.append(clone(n))

            return nnode

        return clone(node)
