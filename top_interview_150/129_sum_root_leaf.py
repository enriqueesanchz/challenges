from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, nums, num):
            if not root:
                return
            
            num = num*10 + root.val
            
            if not root.left and not root.right: # leaf
                nums.append(num)
            
            dfs(root.left, nums, num)
            dfs(root.right, nums, num)

        num = 0
        nums = []
        dfs(root, nums, num)

        sm = 0
        for num in nums:
            sm += num

        return sm
