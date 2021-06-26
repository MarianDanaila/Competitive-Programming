class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n = len(part)
        for ch in s:
            stack.append(ch)
            m = len(stack)
            if m >= n:
                removing = True
                idx1 = n - 1
                idx2 = m - 1
                while idx1 >= 0:
                    if stack[idx2] != part[idx1]:
                        removing = False
                        break
                    idx1 -= 1
                    idx2 -= 1
                if removing:
                    for _ in range(n):
                        stack.pop()
        return "".join(stack)
