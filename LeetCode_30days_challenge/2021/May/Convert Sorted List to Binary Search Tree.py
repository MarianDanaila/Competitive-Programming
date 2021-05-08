from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach1: Convert Linked List to Array
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return
        sorted_array = []
        while head:
            sorted_array.append(head.val)
            head = head.next
        dq = deque()
        n = len(sorted_array)
        mid = (n - 1) // 2
        root = TreeNode(sorted_array[mid])
        dq.append([root, [0, mid - 1], [mid + 1, n - 1]])
        while dq:
            curr, left_interval, right_interval = dq.popleft()
            if left_interval[0] <= left_interval[1]:
                mid_left = left_interval[0] + (left_interval[1] - left_interval[0]) // 2
                left_node = TreeNode(sorted_array[mid_left])
                curr.left = left_node
            if right_interval[0] <= right_interval[1]:
                mid_right = right_interval[0] + (right_interval[1] - right_interval[0]) // 2
                right_node = TreeNode(sorted_array[mid_right])
                curr.right = right_node
            if left_interval[0] <= left_interval[1] and right_interval[0] <= right_interval[1]:
                dq.append([left_node, [left_interval[0], mid_left - 1], [mid_left + 1, left_interval[1]]])
                dq.append([right_node, [right_interval[0], mid_right - 1], [mid_right + 1, right_interval[1]]])
        return root


# Approach2: Recursion
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return
        return self.bst(head, None)

    def bst(self, head, tail):
        slow = fast = head
        if head == tail:
            return
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next
        thead = TreeNode(slow.val)
        thead.left = self.bst(head, slow)
        thead.right = self.bst(slow.next, tail)
        return thead
