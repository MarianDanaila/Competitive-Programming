# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        first_greater = prev = None
        curr = head
        while curr:
            changed_curr = False
            if curr.val < x:
                if first_greater:
                    changed = curr
                    curr = curr.next
                    prev.next = curr
                    if before_first_greater:
                        before_first_greater.next = changed
                    else:
                        head = changed
                    changed.next = first_greater
                    before_first_greater = changed
                    changed_curr = True
            else:
                if not first_greater:
                    first_greater = curr
                    before_first_greater = prev

            if not changed_curr:
                if not prev:
                    prev = curr
                else:
                    prev = prev.next
                curr = curr.next
        return head
