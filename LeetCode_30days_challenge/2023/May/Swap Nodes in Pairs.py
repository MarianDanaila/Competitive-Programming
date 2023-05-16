from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        curr = head
        head = head.next
        prev = None
        while curr and curr.next:
            if prev:
                prev.next = curr.next

            copy_node = curr.next.next
            curr.next.next = curr
            curr.next = copy_node
            prev = curr
            curr = curr.next

        return head
