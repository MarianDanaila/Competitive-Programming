# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


# Approach 1: Iterative
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        dq = deque()
        dq.append([root, -float("inf"), float("inf")])
        while dq:
            curr, lower_bound, upper_bound = dq.popleft()
            if not lower_bound < curr.val < upper_bound:
                return False
            if curr.left:
                dq.append([curr.left, lower_bound, curr.val])
            if curr.right:
                dq.append([curr.right, curr.val, upper_bound])
        return True


# Approach 2: Recursive
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def traversal(node, lower_bound, upper_bound):
            if not node:
                return True
            if not lower_bound < node.val < upper_bound:
                return False

            return traversal(node.left, lower_bound, node.val) and traversal(node.right, node.val, upper_bound)

        return traversal(root, -float("inf"), float("inf"))
