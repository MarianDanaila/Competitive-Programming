# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return
        dq = deque()
        dq.append(root)
        right_side = [root.val]
        while dq:
            rightmost = None
            for _ in range(len(dq)):
                curr = dq.popleft()
                if curr.left:
                    dq.append(curr.left)
                    rightmost = curr.left

                if curr.right:
                    dq.append(curr.right)
                    rightmost = curr.right
            if rightmost:
                right_side.append(rightmost.val)
        return right_side
