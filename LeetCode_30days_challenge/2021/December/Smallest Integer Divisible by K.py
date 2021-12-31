class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        n = length = 1
        for _ in range(K):
            remainder = n % K
            if remainder == 0:
                return length
            n = remainder * 10 + 1
            length += 1
        return -1
