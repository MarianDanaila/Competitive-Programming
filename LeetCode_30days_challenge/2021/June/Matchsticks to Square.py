from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        matchsticks.sort(reverse=True)
        sums = [0, 0, 0, 0]

        def dfs(index):
            if index == n:
                return sums[0] == sums[1] == sums[2] == sums[3]
            for i in range(4):
                if sums[i] + matchsticks[index] <= perimeter // 4:
                    sums[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    sums[i] -= matchsticks[index]
            return False

        return dfs(0)
