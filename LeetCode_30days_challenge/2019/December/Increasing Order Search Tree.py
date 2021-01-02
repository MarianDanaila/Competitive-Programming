# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root):
        if not root:
            return
        stack = []
        inorder = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack[-1]
            stack.pop()
            inorder.append(root)
            root = root.right
        root = inorder[0]
        copy_root = root
        for i in range(1, len(inorder)):
            root.left = None
            root.right = inorder[i]
            root = inorder[i]
        root.left = None
        root.right = None
        return copy_root
