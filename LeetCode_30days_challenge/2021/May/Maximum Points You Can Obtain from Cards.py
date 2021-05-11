from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        sum1 = 0
        sum2 = sum(cardPoints[n - k:])
        max_sum = sum2
        for i in range(k):
            sum1 += cardPoints[i]
            sum2 -= cardPoints[n - k + i]
            max_sum = max(sum1 + sum2, max_sum)
        return max_sum
