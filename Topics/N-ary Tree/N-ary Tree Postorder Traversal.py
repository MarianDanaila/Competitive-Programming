from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Approach 1: Recursive
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        def traversal(root):
            for child in root.children:
                traversal(child)
            postorder_traversal.append(root.val)

        postorder_traversal = []
        traversal(root)
        return postorder_traversal


# Approach 2: Iterative
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        postorder_traversal = []
        stack = [[root, False]]
        while stack:
            curr, visited = stack.pop()
            if visited:
                postorder_traversal.append(curr.val)
            else:
                stack.append([curr, True])
                children = len(curr.children)
                for i in range(children - 1, -1, -1):
                    stack.append([curr.children[i], False])
        return postorder_traversal


# Approach 3: Recursive Modified Preorder
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        def traversal(root):
            preorder_modified.append(root.val)
            children = len(root.children)
            for i in range(children - 1, -1, -1):
                traversal(root.children[i])

        preorder_modified = []
        traversal(root)
        return preorder_modified[::-1]


# Approach 4: Iterative Modified Preorder
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        preorder_modified = []
        while stack:
            curr = stack.pop()
            preorder_modified.append(curr.val)
            for child in curr.children:
                stack.append(child)
        return preorder_modified[::-1]
