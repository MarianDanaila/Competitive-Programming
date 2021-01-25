# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        add = 0
        dummy = l3 = ListNode(0)
        while l1 and l2:
            sum_digits = l1.val + l2.val + add
            add = sum_digits // 10
            l3.next = ListNode(sum_digits % 10)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            add_digit = l1.val + add
            add = add_digit // 10
            l3.next = ListNode(add_digit % 10)
            l3 = l3.next
            l1 = l1.next

        while l2:
            add_digit = l2.val + add
            add = add_digit // 10
            l3.next = ListNode(add_digit % 10)
            l3 = l3.next
            l2 = l2.next

        if add == 1:
            l3.next = ListNode(1)
        return dummy.next
