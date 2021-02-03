# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        fast = head.next
        while fast:
            if fast == head:
                return True
            else:
                if not fast.next:
                    return False
                fast = fast.next.next
                head = head.next
        return False
