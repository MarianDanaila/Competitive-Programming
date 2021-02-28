from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        m = len(toppingCosts)

        for i in range(m):
            toppingCosts.append(toppingCosts[i])
        m += m
        best = float("inf")
        ans = 0

        for i in range(2 ** m):
            cost = 0
            for j in range(m):
                if (i & (1 << j)) > 0:
                    cost += toppingCosts[j]

            for baseCost in baseCosts:
                cost += baseCost
                if abs(target - cost) < best:
                    best = abs(target - cost)
                    ans = cost
                elif abs(target - cost) == best:
                    ans = min(ans, cost)

                if best == 0:
                    return ans
                cost -= baseCost

        return ans
