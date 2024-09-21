from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(root, stack):
            if not root:
                return

            stack.append(root)
            dfs(root.left, stack)
            dfs(root.right, stack)

        stack = []
        dfs(root, stack)

        prev = TreeNode()
        for node in stack:
            prev.left = None
            prev.right = node
            prev = node
