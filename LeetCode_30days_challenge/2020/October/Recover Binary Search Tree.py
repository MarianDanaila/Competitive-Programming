# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    first = TreeNode()
    second = TreeNode()
    prev = TreeNode(-(2**31))

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        self.first.val = self.second.val

    def traverse(self, root: TreeNode):
        if not root:
            return
        self.traverse(root.left)

        if not self.first and self.prev.val >= root.val:
            self.first = self.prev
        if self.first and self.prev.val >= root.val:
            self.second = root

        self.prev = root
        self.traverse(root.right)
