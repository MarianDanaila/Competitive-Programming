# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [[cloned, original]]
        while stack:
            c, o = stack.pop()
            if o is target:
                return c
            if o.left:
                stack.append([c.left, o.left])
            if o.right:
                stack.append([c.right, o.right])
