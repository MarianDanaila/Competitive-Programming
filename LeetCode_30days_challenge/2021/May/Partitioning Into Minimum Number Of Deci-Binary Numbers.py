class Solution:
    def minPartitions(self, n: str) -> int:
        maxim = "0"
        for ch in n:
            if ch > maxim:
                maxim = ch

        return int(maxim)
