class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        good = {'a': 0, 'b': 0, 'l': 0, 'o': 0, 'n': 0}
        for ch in text:
            if ch in good:
                good[ch] += 1

        ans = float("inf")
        for ch in good:
            if ch == 'l' or ch == 'o':
                ans = min(ans, good[ch] // 2)
            else:
                ans = min(ans, good[ch])
        return ans
