# Recursive


class Solution:
    def postorderTraversal(self, root):
        ans = []
        self.helper(root, ans)
        return ans

    def helper(self, root, ans):
        if root:
            self.helper(root.left, ans)
            self.helper(root.right, ans)
            ans.append(root.val)

# Iterative 1
# The first is by postorder using a flag to indicate whether the node has been visited or not.


class Solution2:
    def postorderTraversal(self, root):
        ans = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    ans.append(node.val)
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return ans

# Iterative 2
# The second uses modified preorder(right subtree first).Then reverse the result


class Solution3:
    def postorderTraversal(self, root):
        ans = []
        stack = [root]
        while stack:
            node = stack[-1]
            stack.pop()
            if node:
                # pre-order, right first
                ans.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        # reverse result
        return ans[::-1]



