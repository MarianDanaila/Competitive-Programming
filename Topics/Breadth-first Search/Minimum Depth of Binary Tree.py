# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        min_depth = float("inf")
        while stack:
            root, depth = stack.pop()
            if not root.left and not root.right:  # current node is a leaf
                min_depth = min(min_depth, depth)
            if root.left:
                stack.append([root.left, depth + 1])
            if root.right:
                stack.append([root.right, depth + 1])
        return min_depth


# BFS
from collections import deque


class Solution2:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        depth = 0
        while q:
            depth += 1
            for _ in range(len(q)):
                root = q.popleft()
                if not root.left and not root.right:
                    return depth
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
