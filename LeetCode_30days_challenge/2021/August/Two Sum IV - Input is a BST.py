# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1: O(N) space complexity, where N is the number of nodes in the tree
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nodes = []

        def inorder(node):
            if node:
                inorder(node.left)
                nodes.append(node.val)
                inorder(node.right)

        inorder(root)
        n = len(nodes)
        start, end = 0, n - 1
        while start < end:
            if nodes[start] + nodes[end] == k:
                return True
            elif nodes[start] + nodes[end] < k:
                start += 1
            else:
                end -= 1
        return False


# Approach 2: O(H) space complexity, where H is the height of the tree
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        left, right = [], []
        node = root
        while node:
            left.append(node)
            node = node.left

        node = root
        while node:
            right.append(node)
            node = node.right

        left_node, right_node = left.pop(), right.pop()
        while left_node.val != right_node.val:
            curr_sum = left_node.val + right_node.val
            if curr_sum == k:
                return True
            elif curr_sum < k:
                if left_node.right:
                    left_node = left_node.right
                    while left_node:
                        left.append(left_node)
                        left_node = left_node.left
                left_node = left.pop()
            else:
                if right_node.left:
                    right_node = right_node.left
                    while right_node:
                        right.append(right_node)
                        right_node = right_node.right
                right_node = right.pop()
        return False
