# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        while True:
            if root.val < low:
                root = root.right
            elif root.val > high:
                root = root.left
            else:
                break

        dq = deque()
        dq.append(root)
        while dq:
            curr = dq.popleft()
            if curr.left:
                if curr.left.val >= low:
                    dq.append(curr.left)
                else:
                    curr.left = curr.left.right
                    if curr.left:
                        dq.append(curr)

            if curr.right:
                if curr.right.val <= high:
                    dq.append(curr.right)
                else:
                    curr.right = curr.right.left
                    if curr.right:
                        dq.append(curr)

        return root
