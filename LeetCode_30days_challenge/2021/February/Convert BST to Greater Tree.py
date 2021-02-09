# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative
class Solution1:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = [[root, False]]
        sum_greater = 0
        while stack:
            curr, visited = stack.pop()
            if visited:
                curr.val += sum_greater
                sum_greater = curr.val
            else:
                if curr.left:
                    stack.append([curr.left, False])
                stack.append([curr, True])
                if curr.right:
                    stack.append([curr.right, False])
        return root

# Recursive


class Solution2:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum_greater = 0
        if not root:
            return None

        def traverse(root):
            if not root:
                return 0
            traverse(root.right)
            self.sum_greater += root.val
            root.val = self.sum_greater
            traverse(root.left)
            return root
        return traverse(root)
