from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushall(root)

    def next(self) -> int:
        if self.stack:
            cur = self.stack.pop()

            if cur.right:
                self.pushall(cur.right)

            return cur.val
        return None

    def hasNext(self) -> bool:
        return len(self.stack) != 0

    def pushall(self, cur) -> None:
        while cur:
            self.stack.append(cur)
            cur = cur.left
