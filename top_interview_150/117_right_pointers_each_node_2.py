from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        q = deque([root])
        dummy = Node()

        while q:
            length = len(q)
            prev = dummy
            for _ in range(length):
                curr = q.popleft()

                if curr.left:
                    prev.next = curr.left
                    q.append(curr.left)
                    prev = curr.left
                if curr.right:
                    prev.next = curr.right
                    q.append(curr.right)
                    prev = curr.right
            
        return root
