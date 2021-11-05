# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        dq.append(root)
        left_sum = 0
        while dq:
            curr_node = dq.popleft()
            if curr_node.left:
                if not curr_node.left.left and not curr_node.left.right:
                    left_sum += curr_node.left.val
                dq.append(curr_node.left)
            if curr_node.right:
                dq.append(curr_node.right)
        return left_sum
