from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0, head)
        prev, curr = dummy, head
        dup = 101

        while curr.next:
            if curr.val == curr.next.val:
                dup = curr.val

            if curr.val == dup:
                prev.next = curr.next
            else:
                prev = prev.next

            curr = curr.next

        if curr.val == dup:
            prev.next = None

        return dummy.next
