class Solution:
    def maxProfit(self, k: int, prices):
        n = len(prices)
        if k >= n // 2:
            sell = 0
            buy = -float("inf")
            for price in prices:
                old_sell = sell
                sell = max(sell, buy + price)
                buy = max(buy, old_sell - price)

            return sell
        else:
            dp_ik0 = [0] * (k + 1)
            dp_ik1 = [-float("inf")] * (k + 1)
            for price in prices:
                for j in range(k, 0, -1):
                    dp_ik0[j] = max(dp_ik0[j], dp_ik1[j] + price)
                    dp_ik1[j] = max(dp_ik1[j], dp_ik0[j - 1] - price)
            return dp_ik0[-1]
