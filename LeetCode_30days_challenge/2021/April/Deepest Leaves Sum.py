# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        dq = deque()
        dq.append(root)
        while dq:
            length = len(dq)
            level_sum = 0
            for _ in range(length):
                curr = dq.popleft()
                level_sum += curr.val
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)

        return level_sum
