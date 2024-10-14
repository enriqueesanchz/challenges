from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res
        curr = res

        for _ in range(n):
            dummy = dummy.next

        while dummy.next:
            curr = curr.next
            dummy = dummy.next

        curr.next = curr.next.next
        return res.next
