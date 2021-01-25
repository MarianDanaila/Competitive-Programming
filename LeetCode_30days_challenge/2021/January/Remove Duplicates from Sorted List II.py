# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return ListNode()
        if not head.next:
            return head
        dummy = node = ListNode(0)
        prev = None
        while True:
            if prev is None:
                if head.val < head.next.val:  # assure that it exists next
                    node.next = head
                    node = head
            elif head.next:
                if prev.val < head.val < head.next.val:
                    node.next = head
                    node = head
            else:
                if prev.val < head.val:
                    node.next = head
                    node = head
                node.next = None
                return dummy.next
            prev = head
            head = head.next
