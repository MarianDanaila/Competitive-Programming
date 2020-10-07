# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length = 0
        copy_head = head
        while copy_head:
            length += 1
            copy_head = copy_head.next
        if length == 0:
            return

        k = k % length
        if k == 0:
            return head

        copy_head = head
        index = 0
        ok = True
        while head:
            index += 1
            if index >= length - k + 1:
                if ok:
                    first = ListNode(head.val)
                    ans = first
                    ok = False
                else:
                    curr = ListNode(head.val)
                    first.next = curr
                    first = curr
            head = head.next

        index = 1
        while index <= length - k:
            curr = ListNode(copy_head.val)
            first.next = curr
            first = curr
            index += 1
            copy_head = copy_head.next
        return ans
