from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        stack = [[root, False]]
        while stack:
            node, visited = stack.pop()
            if visited:
                if node.left:
                    node.val += node.left.val
                if node.right:
                    node.val += node.right.val
            else:
                stack.append([node, True])
                if node.right:
                    stack.append([node.right, False])
                if node.left:
                    stack.append([node.left, False])

        dq = deque()
        dq.append(root)
        ans = 1
        while dq:
            len_dq = len(dq)
            for _ in range(len_dq):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                    ans = max(ans, node.left.val * (root.val - node.left.val))
                if node.right:
                    dq.append(node.right)
                    ans = max(ans, node.right.val * (root.val - node.right.val))

        return ans % (10 ** 9 + 7)
