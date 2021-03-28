class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        n = len(s)

        def expand(left, right):
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(n):
            counter += expand(i, i + 1)
            counter += expand(i, i)

        return counter
