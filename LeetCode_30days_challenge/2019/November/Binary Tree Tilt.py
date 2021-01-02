# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.total_tilt = 0

        def valueSum(node):
            if not node:  # if it is a leaf
                return 0

            left_sum = valueSum(node.left)
            right_sum = valueSum(node.right)
            tilt = abs(left_sum - right_sum)
            self.total_tilt += tilt

            return left_sum + right_sum + node.val

        valueSum(root)
        return self.total_tilt
