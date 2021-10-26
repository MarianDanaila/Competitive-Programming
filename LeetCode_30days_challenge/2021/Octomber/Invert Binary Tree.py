# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque()
        if root:
            dq.append(root)
        while dq:
            len_dq = len(dq)
            for _ in range(len_dq):
                curr = dq.popleft()
                left_child = curr.left
                right_child = curr.right
                if curr.right:
                    dq.append(curr.right)

                if curr.left:
                    dq.append(curr.left)
                curr.left = right_child
                curr.right = left_child

        return root
