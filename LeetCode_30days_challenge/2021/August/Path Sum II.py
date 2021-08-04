from collections import deque
from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        dq = deque()
        paths = []
        if root:
            dq.append((root, [root.val], root.val))
        while dq:
            len_dq = len(dq)
            for _ in range(len_dq):
                node, path, path_sum = dq.popleft()
                if not node.left and not node.right:  # it is a leaf
                    if path_sum == targetSum:
                        paths.append(path)
                        continue
                if node.left:
                    next_path = path.copy()
                    next_path.append(node.left.val)
                    dq.append((node.left, next_path, path_sum + node.left.val))

                if node.right:
                    next_path = path.copy()
                    next_path.append(node.right.val)
                    dq.append((node.right, next_path, path_sum + node.right.val))

        return paths
