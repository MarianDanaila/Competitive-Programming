# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        def buildTree(left, right):
            if left > right:
                return None
            mid = left + (right-left) // 2
            new_node = TreeNode(nums[mid])
            new_node.left = buildTree(left, mid-1)
            new_node.right = buildTree(mid+1, right)
            return new_node
        return buildTree(0, len(nums)-1)
