from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, nodes):
            if not root:
                return
            
            dfs(root.left, nodes)
            nodes.append(root.val) # inorder, min diff is always on closest elements
            dfs(root.right, nodes)

        nodes = []
        dfs(root, nodes)
        
        dif = float('inf')
        for i in range(len(nodes)-1):
            dif = min(dif, abs(nodes[i]-nodes[i+1]))

        return dif
