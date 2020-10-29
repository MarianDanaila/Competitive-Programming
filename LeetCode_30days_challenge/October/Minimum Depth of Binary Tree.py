# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque()
        q.append([root, 1])
        while q:
            for _ in range(len(q)):
                root, level = q.popleft()
                if not root.left and not root.right:
                    return level
                if root.left:
                    q.append([root.left, level+1])
                if root.right:
                    q.append([root.right, level+1])
