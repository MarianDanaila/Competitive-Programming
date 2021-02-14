class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 0
        i = length = 1
        n = len(s)
        while i < n:
            if s[i] == s[i-1]:
                length += 1
            else:
                count += length*(length+1) // 2
                length = 1
            i += 1
        count += length*(length+1) // 2
        return count % (10 ** 9 + 7)
