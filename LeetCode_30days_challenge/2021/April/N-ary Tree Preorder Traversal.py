from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Iterative
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        preorder = []
        if not root:
            return preorder
        stack = [root]
        while stack:
            curr = stack.pop()
            preorder.append(curr.val)
            len_children = len(curr.children)
            for i in range(len_children - 1, -1, -1):
                stack.append(curr.children[i])
        return preorder


# Recursive
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        inorder = []
        if not root:
            return inorder

        def helper(node):
            inorder.append(node.val)
            for child in node.children:
                helper(child)

        helper(root)
        return inorder
