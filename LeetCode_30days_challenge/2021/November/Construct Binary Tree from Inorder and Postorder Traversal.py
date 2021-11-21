from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        n = len(inorder)
        map_inorder = {}
        for i in range(n):
            map_inorder[inorder[i]] = i
        self.postorder_idx = n - 1

        def recur(low, high):
            if low > high:
                return None
            new_node = TreeNode(postorder[self.postorder_idx])
            self.postorder_idx -= 1
            inorder_idx = map_inorder[new_node.val]
            new_node.right = recur(inorder_idx + 1, high)
            new_node.left = recur(low, inorder_idx - 1)
            return new_node

        return recur(0, n - 1)
