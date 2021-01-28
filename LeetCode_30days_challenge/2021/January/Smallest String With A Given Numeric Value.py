class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        out = []
        for i in range(n):
            if k - ((n - i - 1) * 26) <= 0:
                out.append('a')
                k -= 1
            else:
                out.append(chr(k - ((n - i - 1) * 26) + 96))
                k = (n - i - 1) * 26

        return ''.join(out)
