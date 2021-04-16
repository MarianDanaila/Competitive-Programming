class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if k == 1:
            return ""
        stack = []
        for ch in s:
            if not stack or stack[-1][0] != ch:
                stack.append([ch, 1])
            else:
                if stack[-1][1] == k - 1:
                    for _ in range(k - 1):
                        stack.pop()
                else:
                    stack.append([ch, stack[-1][1] + 1])

        n = len(stack)
        for i in range(n):
            stack[i] = stack[i][0]
        return "".join(stack)
