from typing import List
# DP


class Solution:
    def maxAlternatingSum(self, prices: List[int]) -> int:
        # It is impossible to sell stock on first day, set -infinity as initial value for cur_hold
        cur_hold, cur_not_hold = 0, -float("inf")

        for stock_price in prices:
            prev_hold, prev_not_hold = cur_hold, cur_not_hold

            # either keep not-hold, or sell out stock today at stock price
            cur_not_hold = max(prev_not_hold, prev_hold + stock_price)

            # either keep hold, or buy in stock today at stock price
            cur_hold = max(prev_hold, prev_not_hold - stock_price)

        # maximum profit must be in not-hold state
        return cur_not_hold if prices else 0
