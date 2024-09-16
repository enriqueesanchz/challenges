# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        v = set()

        while head:
            if head not in v:
                v.add(head)
                head = head.next
            else:
                return True

        return False
