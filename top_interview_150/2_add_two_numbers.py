# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2:
            curr.next = ListNode()
            curr = curr.next
            
            sm = carry + (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0)
            curr.val = sm % 10
            carry = sm // 10

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            
        if carry != 0:
            curr.next = ListNode()
            curr = curr.next
            curr.val = carry

        return dummy.next
