# Approach 1
# Space Complexity: O(N) where N is number of nodes in BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.index = -1
        stack = []
        self.inorder = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            self.inorder.append(root.val)
            root = root.right

    def next(self) -> int:
        self.index += 1
        return self.inorder[self.index]

    def hasNext(self) -> bool:

        return self.index + 1 != len(self.inorder)

# Approach 2
# Space Complexity: O(H) where H is height of BST


class BSTIterator2:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.dive_left(root)

    def dive_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        top = self.stack.pop()
        if top.right:
            self.dive_left(top.right)
        return top.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
