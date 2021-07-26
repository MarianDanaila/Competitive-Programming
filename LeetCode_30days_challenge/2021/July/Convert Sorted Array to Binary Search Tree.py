from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        dq = deque()
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        dq.append([root, 0, mid - 1, mid + 1, len(nums) - 1])
        while dq:
            curr, left_lower, left_upper, right_lower, right_upper = dq.popleft()
            if left_lower <= left_upper:
                left_mid = (left_lower + left_upper) // 2
                curr.left = TreeNode(nums[left_mid])
                dq.append([curr.left, left_lower, left_mid - 1, left_mid + 1, left_upper])

            if right_lower <= right_upper:
                right_mid = (right_lower + right_upper) // 2
                curr.right = TreeNode(nums[right_mid])
                dq.append([curr.right, right_lower, right_mid - 1, right_mid + 1, right_upper])
        return root
