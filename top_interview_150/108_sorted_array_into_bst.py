from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        idx = n//2

        def tree(root, l, r):
            if not l and not r:
                return

            lidx = len(l)//2 
            ridx = len(r)//2

            if len(l):
                root.left = TreeNode(l[lidx]) 
            if len(r):
                root.right = TreeNode(r[ridx])

            tree(root.left, l[:lidx], l[lidx+1:])
            tree(root.right, r[:ridx], r[ridx+1:])

        root = TreeNode(nums[idx])
        tree(root, nums[:idx], nums[idx+1:])
        return root
