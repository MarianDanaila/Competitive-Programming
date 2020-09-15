
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from collections import deque


class Solution:
    def levelOrder(self, root: 'Node'):
        if not root:
            return
        q = deque()
        q.append(root)
        levels = [[root.val]]
        while q:
            level = []
            for _ in range(len(q)):
                root = q.popleft()

                for child in root.children:
                    level.append(child.val)
                    q.append(child)
            if level:
                levels.append(level)
        return levels
