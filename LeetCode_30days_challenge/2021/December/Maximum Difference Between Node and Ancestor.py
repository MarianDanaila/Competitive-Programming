from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        dq.append([root, root.val, root.val])
        max_diff = 0
        while dq:
            curr, minim, maxim = dq.popleft()
            if curr.left:
                max_diff = max(max_diff, max(abs(curr.left.val - minim), abs(curr.left.val - maxim)))
                dq.append([curr.left, min(minim, curr.left.val), max(maxim, curr.left.val)])
            if curr.right:
                max_diff = max(max_diff, max(abs(curr.right.val - minim), abs(curr.right.val - maxim)))
                dq.append([curr.right, min(minim, curr.right.val), max(maxim, curr.right.val)])
        return max_diff
