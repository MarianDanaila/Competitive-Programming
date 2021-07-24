# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        stack = [[root, False]]
        while stack:
            curr, visited = stack.pop()
            if visited:
                if curr.left and curr.left.val == -1:
                    curr.left = None
                if curr.right and curr.right.val == -1:
                    curr.right = None

                if not curr.left and not curr.right and curr.val == 0:
                    curr.val = -1

            else:
                stack.append([curr, True])
                if curr.right:
                    stack.append([curr.right, False])
                if curr.left:
                    stack.append([curr.left, False])

        if root.val == -1:
            root = None
        return root
