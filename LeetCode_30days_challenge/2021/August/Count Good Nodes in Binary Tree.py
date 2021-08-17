from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        dq = deque()
        good = 1
        dq.append([root, root.val])
        while dq:
            len_dq = len(dq)
            for _ in range(len_dq):
                node, greatest_so_far = dq.popleft()
                if node.left:
                    if node.left.val >= greatest_so_far:
                        good += 1
                    dq.append([node.left, max(greatest_so_far, node.left.val)])

                if node.right:
                    if node.right.val >= greatest_so_far:
                        good += 1
                    dq.append([node.right, max(greatest_so_far, node.right.val)])

        return good
