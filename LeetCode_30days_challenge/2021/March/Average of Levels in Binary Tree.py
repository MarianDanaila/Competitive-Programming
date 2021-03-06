# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        dq = deque()
        avg = []
        dq.append(root)
        while dq:
            level_sum = level_cnt = 0
            for _ in range(len(dq)):
                curr = dq.popleft()
                level_sum += curr.val
                level_cnt += 1
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)

            avg.append(level_sum / level_cnt)
        return avg
