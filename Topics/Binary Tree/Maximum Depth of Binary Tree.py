# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Approach 1: Top-Down


class Solution:
    def __init__(self):
        self.max_depth = 0

    def maxDepth(self, root: TreeNode) -> int:

        def traverse(node, depth):
            if not node:
                return
            if not node.left and not node.right:
                self.max_depth = max(self.max_depth, depth)
            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)

        traverse(root, 1)
        return self.max_depth


# Approach 2: Bottom-Up


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)
