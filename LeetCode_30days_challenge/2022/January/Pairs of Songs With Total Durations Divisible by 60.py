from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = {}
        pairs = 0
        for song in time:
            remainder = song % 60
            if remainder in remainders:
                remainders[remainder] += 1
            else:
                remainders[remainder] = 1
        for remainder in remainders:
            if remainder == 30 or remainder == 0:
                pairs += remainders[remainder] * (remainders[remainder] - 1) // 2
            else:
                if 60 - remainder in remainders:
                    pairs += remainders[remainder] * remainders[60 - remainder]
            remainders[remainder] = 0
        return pairs
