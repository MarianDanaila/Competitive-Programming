# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# Iterative Approach
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        max_depth = 1
        while stack:
            root, depth = stack.pop()
            max_depth = max(max_depth, depth)
            children = root.children
            for child in children:
                stack.append([child, depth + 1])
        return max_depth
