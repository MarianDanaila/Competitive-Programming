# Recursive

class Solution:
    def inorderTraversal(self, root):
        ans = []
        self.solve(root, ans)
        return ans

    def solve(self, root, ans):
        if root:
            self.solve(root.left, ans)
            ans.append(root.val)
            self.solve(root.right, ans)
        return ans

# Iterative

class Solution2:
    def inorderTraversal(self, root):
        stack = []
        ans = []
        while root or len(stack) > 0:
            while root:
                stack.append(root)
                root = root.left
            root = stack[-1]
            stack.pop()
            ans.append(root.val)
            root = root.right
        return ans

# Morris Method
class Solution3:
    def inorderTraversal(self, root):
        ans = []
        curr = root
        while curr:
            if not curr.left:
                ans.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right:
                    pre = pre.right
                pre.right = curr
                temp = curr
                curr = curr.left
                temp.left = None
        return ans
