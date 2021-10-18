# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [[-float("inf"), preorder[0], float("inf"), root]]
        n = len(preorder)
        for i in range(1, n):
            curr_val = preorder[i]
            while True:
                minimum, last, maximum, last_node = stack[-1]
                if minimum < curr_val < last:
                    new_node = TreeNode(curr_val)
                    last_node.left = new_node
                    stack.append([minimum, curr_val, last, new_node])
                    break
                elif last < curr_val < maximum:
                    new_node = TreeNode(curr_val)
                    last_node.right = new_node
                    stack.pop()
                    stack.append([last, curr_val, maximum, new_node])
                    break
                else:
                    stack.pop()
        return root
