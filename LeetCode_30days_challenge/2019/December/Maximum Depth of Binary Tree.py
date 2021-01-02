# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        dq = deque()
        dq.append(root)
        level = 0
        while dq:
            level += 1
            for _ in range(len(dq)):
                curr = dq.popleft()
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)

        return level
