# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        dq = deque()
        dq.append([root, -float("inf"), float("inf")])
        while dq:
            root, lower, upper = dq.popleft()
            left_child = root.left
            right_child = root.right
            if left_child:
                if root.val > left_child.val > lower:
                    dq.append([left_child, lower, root.val])
                else:
                    return False

            if right_child:
                if root.val < right_child.val < upper:
                    dq.append([right_child, root.val, upper])
                else:
                    return False
        return True
