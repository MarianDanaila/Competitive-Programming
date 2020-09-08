# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Approach 1 Iterative
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        max_depth = 1
        stack = [[root, 1]]
        while stack:
            root, depth = stack.pop()
            if root:
                max_depth = max(max_depth, depth)
                stack.append([root.left, depth + 1])
                stack.append([root.right, depth + 1])

        return max_depth

