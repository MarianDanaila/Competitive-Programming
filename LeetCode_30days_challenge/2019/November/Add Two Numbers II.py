# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack = []
        length_l1 = length_l2 = 0
        node1 = l1
        node2 = l2
        while node1:
            length_l1 += 1
            node1 = node1.next

        while node2:
            length_l2 += 1
            node2 = node2.next

        if length_l1 >= length_l2:
            start = length_l1 - length_l2
            i = 0
            while i < start:
                stack.append(l1.val)
                l1 = l1.next
                i += 1

        else:
            start = length_l2 - length_l1
            i = 0
            while i < start:
                stack.append(l2.val)
                l2 = l2.next
                i += 1

        while l1:
            stack.append(l1.val + l2.val)
            l1 = l1.next
            l2 = l2.next
        add = 0
        last_node = None

        while stack:
            curr_sum = stack.pop()
            curr_sum += add
            curr_node = ListNode(curr_sum % 10)
            if last_node:
                curr_node.next = last_node
            last_node = curr_node
            add = curr_sum // 10
        if add:
            curr_node = ListNode(1)
            curr_node.next = last_node
            last_node = curr_node
        return last_node
