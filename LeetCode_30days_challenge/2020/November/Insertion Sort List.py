# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head
        curr1 = head.next
        while curr1:
            prev_curr2 = None
            curr2 = head
            while curr2:
                if curr2 == curr1:
                    break
                if curr1.val < curr2.val:
                    if not prev_curr2:
                        # insert curr1 as head
                        new_head = ListNode(curr1.val)
                        new_head.next = curr2
                        head = new_head
                    else:
                        new_node = ListNode(curr1.val)
                        prev_curr2.next = new_node
                        new_node.next = curr2
                    break
                else:
                    prev_curr2 = curr2
                    curr2 = curr2.next
            # find prev of curr1 for deleting curr1
            if curr2 == curr1:
                curr1 = curr1.next
                continue
            while curr2 != curr1:
                prev_curr1 = curr2
                curr2 = curr2.next
            # unlink curr1
            curr1 = curr1.next
            prev_curr1.next = curr1

        return head
