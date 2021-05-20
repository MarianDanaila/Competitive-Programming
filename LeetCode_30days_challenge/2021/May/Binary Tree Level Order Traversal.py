from typing import List
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        dq = deque()
        if not root:
            return levels
        dq.append(root)
        levels.append([root.val])
        while dq:
            len_dq = len(dq)
            level = []
            for _ in range(len_dq):
                curr = dq.popleft()
                if curr.left:
                    level.append(curr.left.val)
                    dq.append(curr.left)
                if curr.right:
                    level.append(curr.right.val)
                    dq.append(curr.right)
            if level:
                levels.append(level)
        return levels
