class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(",")
        n = len(preorder)
        if preorder[0] == '#':
            return n == 1
        stack = [preorder[0]]

        for idx in range(1, n):
            if preorder[idx] != '#':
                stack.append(preorder[idx])
            else:
                if not stack:
                    return idx == n - 1
                stack.pop()
        return False
