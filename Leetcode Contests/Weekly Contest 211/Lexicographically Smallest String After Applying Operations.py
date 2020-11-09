class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        stack = [s]
        seen = set()
        ans = s
        while stack:
            s = stack.pop()
            if s < ans:
                ans = s
            first_s = [None] * len(s)
            # first operation
            for i in range(1, len(s), 2):
                first_s[i-1] = s[i-1]
                first_s[i] = str((int(s[i])+a) % 10)
            if len(s) % 2 != 0:
                first_s[-1] = s[-1]
            first_s = "".join(first_s)
            if first_s not in seen:
                stack.append(first_s)
                seen.add(first_s)
            # second operation
            second_s = [None] * len(s)
            for i in range(len(s)):
                second_s[(i+b) % len(s)] = s[i]
            second_s = "".join(second_s)
            if second_s not in seen:
                stack.append(second_s)
                seen.add(second_s)
        return ans
