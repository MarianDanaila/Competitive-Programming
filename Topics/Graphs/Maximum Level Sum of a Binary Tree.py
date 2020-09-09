# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def maxLevelSum(self, root: TreeNode):
        if not root:
            return
        q = deque()
        q.append(root)
        max_sum = 0
        x = 1
        level = 0
        while q:
            curr_sum = 0
            level += 1
            for _ in range(len(q)):
                root = q.popleft()
                curr_sum += root.val
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            if curr_sum > max_sum:
                max_sum = curr_sum
                x = level
        return x
