from typing import Optional
from collections import defaultdict

# Definition for a Node.
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        origin = head
        v = defaultdict(list)
        
        dummy = Node(0)
        curr = dummy
        while head:        
            curr.next = Node(head.val)
            curr = curr.next

            if head.random != None:
                v[head.random].append(curr)
            
            head = head.next
        
        head = origin
        curr = dummy.next
        while head:
            if head in v:
                for c in v[head]:
                    c.random = curr
        
            head = head.next
            curr = curr.next

        return dummy.next
