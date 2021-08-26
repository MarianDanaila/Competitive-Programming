class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(",")
        n = len(preorder)
        if preorder[0] == '#':
            return n == 1
        idx = 0
        stack = [preorder[idx]]

        for idx in range(1, n):
            if preorder[idx] != '#':
                stack.append(preorder[idx])
            else:
                if not stack:
                    return idx == n - 1
                stack.pop()
