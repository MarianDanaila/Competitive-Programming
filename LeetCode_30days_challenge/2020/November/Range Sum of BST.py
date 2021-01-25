# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        total_sum = 0
        stack = [root]
        while stack:
            curr = stack.pop()
            if low <= curr.val <= high:
                total_sum += curr.val
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
            elif curr.val < low:
                if curr.right:
                    stack.append(curr.right)
            else:
                if curr.left:
                    stack.append(curr.left)
        return total_sum
