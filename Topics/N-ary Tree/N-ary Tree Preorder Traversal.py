from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Approach 1: Recursive
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def preorder(root):
            if root:
                preorder_traversal.append(root.val)
                for child in root.children:
                    preorder(child)

        preorder_traversal = []
        preorder(root)
        return preorder_traversal


# Approach 2: Iterative
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = []
        if root:
            stack.append(root)
        preorder = []
        while stack:
            curr = stack.pop()
            preorder.append(curr.val)
            children = len(curr.children)
            for i in range(children - 1, -1, -1):
                stack.append(curr.children[i])
        return preorder
