class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        stack = []
        ones_changed = ones_unchanged = 0
        for i in range(n):
            if s[i] == '1':
                ones_unchanged += 1
        flips = ones_unchanged  # string formed just with 0s
        for i in range(n):
            flips = min(flips, n - i - ones_unchanged + ones_changed)
            if s[i] == '1':
                ones_changed += 1
                ones_unchanged -= 1
        return flips
