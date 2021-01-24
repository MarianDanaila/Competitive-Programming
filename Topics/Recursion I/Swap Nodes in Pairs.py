# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Approach 1 modifying only the values
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        self.helper(head)
        return head

    def helper(self, node):
        if not node:
            return
        if not node.next:
            return

        self.swapPairs(node.next.next)
        node.val, node.next.val = node.next.val, node.val


# Approach 2 modifying the nodes themselves
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        nxt = head.next
        head.next = self.swapPairs(head.next.next)
        nxt.next = head
        return nxt
