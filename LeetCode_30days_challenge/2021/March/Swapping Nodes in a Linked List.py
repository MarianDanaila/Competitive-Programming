# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        length = 0
        curr = head
        while curr:
            length += 1
            if length == k:
                first = curr
            curr = curr.next
        curr = head
        while curr:
            if length == k:
                first.val, curr.val = curr.val, first.val
            length -= 1
            curr = curr.next
        return head
