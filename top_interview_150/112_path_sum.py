from typing import Optional

# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, target, sm):
            if not root:
                return False

            if not root.left and not root.right: # if leaf
                return target == sm + root.val

            return dfs(root.left, target, sm+root.val) or dfs(root.right, target, sm+root.val)

        return dfs(root, targetSum, 0)
