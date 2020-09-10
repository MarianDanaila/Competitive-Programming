# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal = 0
        while head:
            decimal = decimal * 2 + head.val % 2
            head = head.next
        return decimal


class Solution2:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal = 0
        while head:
            decimal = decimal << 1 | head.val
            head = head.next
        return decimal
