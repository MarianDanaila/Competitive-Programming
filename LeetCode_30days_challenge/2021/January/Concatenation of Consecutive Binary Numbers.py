class Solution:
    def concatenatedBinary(self, n: int) -> int:

        bits = ans = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                bits += 1
            ans = ((ans << bits) | i) % (10 ** 9 + 7)

        return ans
