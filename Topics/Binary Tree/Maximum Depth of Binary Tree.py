# TOP-DOWN
class Solution:
    def maxDepth(self, root):
        self.answer = 0
        def helper(root, depth):
            if not root:
                return
            if not root.left and not root.right:
                self.answer = max(self.answer, depth)
            else:
                helper(root.left, depth+1)
                helper(root.right, depth+1)
        helper(root,1)
        return self.answer

# BOTTOM-UP
class Solution:
    def maxDepth(self, root):
        if not root:
            return
        else:
            left_depth = self.maxDepth(root.left)
            right_depth =self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1

