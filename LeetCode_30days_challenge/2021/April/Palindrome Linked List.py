# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        index = 0
        start = head
        while index < length // 2:
            head = head.next
            index += 1

        prev = None
        while head:
            next_head = head.next
            head.next = prev
            prev = head
            head = next_head
        if length % 2 != 0:
            length -= 1

        while index < length:
            if start.val != prev.val:
                return False
            start = start.next
            prev = prev.next
            index += 1
        return True
