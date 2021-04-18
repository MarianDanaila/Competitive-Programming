# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = delayed = head
        diff = n + 1
        while fast:
            if diff > 0:
                diff -= 1
            else:
                delayed = delayed.next
            fast = fast.next
        if diff == 1:
            return head.next
        else:
            delayed.next = delayed.next.next
        return head

