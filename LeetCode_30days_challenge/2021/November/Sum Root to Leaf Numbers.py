# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        dq.append([root, root.val])
        total_sum = 0
        while dq:
            len_dq = len(dq)
            for _ in range(len_dq):
                curr, path = dq.popleft()
                if not curr.left and not curr.right:
                    total_sum += path
                if curr.left:
                    dq.append([curr.left, path * 10 + curr.left.val])
                if curr.right:
                    dq.append([curr.right, path * 10 + curr.right.val])
        return total_sum
