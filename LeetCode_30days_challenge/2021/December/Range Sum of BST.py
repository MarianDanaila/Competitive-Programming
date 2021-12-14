from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        range_sum = 0
        while stack:
            curr_node = stack.pop()
            if low <= curr_node.val <= high:
                if low != curr_node.val and curr_node.left:
                    stack.append(curr_node.left)
                if high != curr_node.val and curr_node.right:
                    stack.append(curr_node.right)
                range_sum += curr_node.val
            elif low > curr_node.val:
                if curr_node.right:
                    stack.append(curr_node.right)
            else:
                if curr_node.left:
                    stack.append(curr_node.left)
        return range_sum
