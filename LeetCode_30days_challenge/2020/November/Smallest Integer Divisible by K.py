class Solution:
    def smallestRepunitDivByK(self, K: int):
        remainder = 0
        for length_n in range(1, K+1):
            remainder = (remainder * 10 + 1) % K
            if remainder == 0:
                return length_n
        return -1
