# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow = head.next
        fast = head.next.next
        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next
        if fast is None or fast.next is None:
            return None
        entry = head
        while entry != slow:
            entry = entry.next
            slow = slow.next
        return entry
