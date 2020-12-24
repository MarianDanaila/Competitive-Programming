# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        if not head:
            return
        if head.next:
            h = head.next
        else:
            return head

        curr = head
        first = True
        while True:
            nxt = curr.next
            third = curr.next.next

            if not first:
                prev.next = nxt
            else:
                first = False
            nxt.next = curr
            curr.next = third
            prev = curr

            if curr.next:
                if curr.next.next:
                    curr = curr.next
                else:
                    break
            else:
                break
        return h
