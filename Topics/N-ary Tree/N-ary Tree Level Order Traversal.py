from collections import deque
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        dq = deque()
        dq.append(root)
        levels = [[root.val]]
        while dq:
            level = []
            len_dq = len(dq)
            for _ in range(len_dq):
                curr = dq.popleft()
                for child in curr.children:
                    level.append(child.val)
                    dq.append(child)
            if level:
                levels.append(level)
        return levels
