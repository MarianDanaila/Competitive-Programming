class Solution:
    def maximumWealth(self, accounts) -> int:
        max_wealth = 0
        for i in range(len(accounts)):
            max_wealth = max(max_wealth, sum(accounts[i]))
        return max_wealth
