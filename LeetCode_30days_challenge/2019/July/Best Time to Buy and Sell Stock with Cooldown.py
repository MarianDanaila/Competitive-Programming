# Space-complexity: O(N)
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        s0 = [0] * len(prices)
        s1 = [0] * len(prices)
        s2 = [0] * len(prices)
        s1[0] = -prices[0]
        s2[0] = -float("inf")
        for i in range(1, len(prices)):
            s0[i] = max(s0[i - 1], s2[i - 1])
            s1[i] = max(s1[i - 1], s0[i - 1] - prices[i])
            s2[i] = s1[i - 1] + prices[i]

        return max(s0[-1], s2[-1])

# Space-complexity: O(1)
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        s0 = 0
        s1 = -prices[0]
        s2 = -float("inf")
        for i in range(1, len(prices)):
            last_s2 = s2
            s2 = s1 + prices[i]
            s1 = max(s1, s0 - prices[i])
            s0 = max(s0, last_s2)

        return max(s0, s2)
