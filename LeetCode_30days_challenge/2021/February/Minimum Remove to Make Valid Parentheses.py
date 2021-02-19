class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        deletions = []
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if not stack:
                    deletions.append(i)
                else:
                    stack.pop()
        for i in stack:
            deletions.append(i)
        new_s = []
        j = 0
        for i in range(n):
            if j < len(deletions) and i == deletions[j]:
                j += 1
            else:
                new_s.append(s[i])
        return "".join(new_s)
