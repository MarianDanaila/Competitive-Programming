# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode):
        self.result = 0

        def helper(node, curr_min, curr_max):
            if not node:
                return
            self.result = max(self.result, abs(curr_min-node.val), abs(curr_max-node.val))
            curr_min = min(curr_min, node.val)
            curr_max = max(curr_max, node.val)
            helper(node.left, curr_min, curr_max)
            helper(node.right, curr_min, curr_max)
        helper(root, root.val, root.val)
        return self.result


# Another approach using max - min on all routes from root to leaf
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode):
        stack = [[root, root.val, root.val]]
        ans = 0
        while stack:
            node, curr_min, curr_max = stack.pop()
            ans = max(ans, abs(node.val-curr_min), abs(node.val-curr_max))
            curr_min = min(curr_min, node.val)
            curr_max = max(curr_max, node.val)
            if node.left:
                stack.append([node.left, curr_min, curr_max])
            if node.right:
                stack.append([node.right, curr_min, curr_max])
        return ans
