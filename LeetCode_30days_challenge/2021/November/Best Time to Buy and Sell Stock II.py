from typing import List

# Solution 1


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        i = 1
        while i < n:
            while i < n and prices[i - 1] >= prices[i]:
                i += 1
            buy = prices[i - 1]
            while i < n and prices[i - 1] <= prices[i]:
                i += 1
            sell = prices[i - 1]
            profit += sell - buy
        return profit


# Solution 2
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i - 1] < prices[i]:
                profit += prices[i] - prices[i - 1]
        return profit
"""