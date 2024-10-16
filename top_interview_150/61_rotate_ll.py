from typing import Optional
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head

        dummy = ListNode()
        dummy.next = head
        q = deque([])

        count = 0
        while head:
            count += 1
            q.append(head)
            if len(q) > k+1:
                q.popleft()
            head = head.next

        if k >= count:
            k = k % count

        if k == 0:
            return dummy.next

        while k > 0 and len(q) > 1:
            k -= 1
            node = q.pop()
            node.next = dummy.next
            dummy.next = node

        node = q.pop()
        node.next = None
        return dummy.next
