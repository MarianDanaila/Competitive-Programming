# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        if root:
            stack.append(root)
        while stack:
            curr = stack.pop()
            if curr == root:
                new_root = root
            else:
                new_root.left = None
                new_root.right = curr
                new_root = new_root.right
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return root
