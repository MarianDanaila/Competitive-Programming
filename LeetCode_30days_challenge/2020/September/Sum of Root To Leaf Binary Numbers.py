# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root):
        if not root:
            return
        if root.val == 0:
            stack = [[root, 0]]
        else:
            stack = [[root, 1]]
        s = 0
        while stack:
            root, nr = stack.pop()
            if not root.left and not root.right:
                s += nr
            elif not root.left:
                stack.append([root.right, nr*2 + root.right.val % 2])
            elif not root.right:
                stack.append([root.left, nr*2 + root.left.val % 2])
            else:
                stack.append([root.right, nr*2 + root.right.val % 2])
                stack.append([root.left, nr*2 + root.left.val % 2])
        return s
