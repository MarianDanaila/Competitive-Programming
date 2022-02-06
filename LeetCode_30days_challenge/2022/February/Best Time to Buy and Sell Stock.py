from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 10000
        for price in prices:
            if price < buy:
                buy = price
            else:
                max_profit = max(max_profit, price - buy)
        return max_profit
