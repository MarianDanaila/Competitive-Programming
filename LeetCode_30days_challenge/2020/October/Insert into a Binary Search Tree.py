# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        cur_root = root
        while cur_root:
            last_root = cur_root
            if val < cur_root.val:
                cur_root = cur_root.left
                position = 0
            else:
                cur_root = cur_root.right
                position = 1
        if position == 0:
            last_root.left = TreeNode(val)
        else:
            last_root.right = TreeNode(val)
        return root
