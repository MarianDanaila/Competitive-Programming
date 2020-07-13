# Iterative
class Solution:
    def preorderTraversal(self, root):
        stack = [root]
        ans = []
        while len(stack) > 0:
            node = stack[-1]
            stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans

# Recursive
class Solution:
    def preorderTraversal(self, root):
        stack = []
        self.dfs(root, stack)
        return stack

    def dfs(self, root, stack):
        if root:
            stack.append(root.val)
            self.dfs(root.left, stack)
            self.dfs(root.right, stack)
        else:
            return