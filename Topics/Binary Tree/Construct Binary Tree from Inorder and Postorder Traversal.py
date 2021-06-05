# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        map_inorder = {}
        n = len(inorder)
        for i in range(n):
            map_inorder[inorder[i]] = i

        def recur(low, high):
            if low > high:
                return None

            node = TreeNode(postorder.pop())
            idx = map_inorder[node.val]
            node.right = recur(idx + 1, high)
            node.left = recur(low, idx - 1)

            return node

        return recur(0, n - 1)
