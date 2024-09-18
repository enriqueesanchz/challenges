from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left-1):
            prev = prev.next

        stack = []
        curr = prev.next
        for _ in range(right-left+1):
            stack.append(curr)
            curr = curr.next # ends being right+1

        while stack:
            prev.next = stack.pop() # left-1 -> right and so on
            prev = prev.next

        prev.next = curr # left -> right+1

        return dummy.next
