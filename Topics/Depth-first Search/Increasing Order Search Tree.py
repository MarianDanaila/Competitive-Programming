# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1 with DFS
# Space-complexity: O(N)
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        head = curr = TreeNode()

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            curr.right = TreeNode(root.val)
            curr = curr.right
            root = root.right
        return head.right

# Approach 2 with DFS and Relinking
# Space-complexity : O(H) where h is height of binary tree
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if root:
                inorder(root.left)
                root.left = None
                self.curr.right = root
                self.curr = self.curr.right
                inorder(root.right)

        head = self.curr = TreeNode()
        inorder(root)
        return head.right