"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
"""


def dfs(self, root, answer):
    if root.left is not None:
        dfs(self, root.left, answer)
    answer.append(root.val)
    if root.right is not None:
        dfs(self, root.right, answer)


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        answer = []
        dfs(self, root, answer)
        return answer[k - 1]