class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack:
                if abs(ord(s[i]) - ord(stack[-1])) == 32:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        ans = ""
        for i in stack:
            ans += i
        return ans
