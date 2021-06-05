# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        map_inorder = {}
        n = len(preorder)
        for i in range(n):
            map_inorder[inorder[i]] = i
        idx_preorder = 0

        def recur(low, high):
            nonlocal idx_preorder
            if low > high:
                return None

            node = TreeNode(preorder[idx_preorder])
            idx_preorder += 1
            idx = map_inorder[node.val]
            node.left = recur(low, idx - 1)
            node.right = recur(idx + 1, high)
            return node

        return recur(0, n - 1)
