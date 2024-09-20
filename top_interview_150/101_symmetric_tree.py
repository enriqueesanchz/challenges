from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def is_mirror(n1: Optional[TreeNode], n2: Optional[TreeNode]):
            if not n1 and not n2:
                return True
            
            if n1 and n2 and n1.val == n2.val:
                return is_mirror(n1.left, n2.right) and is_mirror(n1.right, n2.left)
            
            return False

        return is_mirror(root.left, root.right)
