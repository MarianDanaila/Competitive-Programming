from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        sorted_nodes = []
        stack1 = []
        stack2 = []
        while stack1 or root1 or stack2 or root2:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left

            if not stack2 or (stack1 and stack1[-1].val <= stack2[-1].val):
                root1 = stack1.pop()
                sorted_nodes.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                sorted_nodes.append(root2.val)
                root2 = root2.right
        return sorted_nodes
