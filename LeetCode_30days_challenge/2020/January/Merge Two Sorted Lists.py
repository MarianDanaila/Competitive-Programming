# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode(0)
        while l1 or l2:
            if not l1:
                curr.next = l2
                curr = l2
                l2 = l2.next
            elif not l2:
                curr.next = l1
                curr = l1
                l1 = l1.next
            else:
                if l1.val <= l2.val:
                    curr.next = l1
                    curr = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    curr = l2
                    l2 = l2.next
        return head.next
