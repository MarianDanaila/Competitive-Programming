class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        possible = []
        minutes = targetSeconds // 60
        seconds = targetSeconds % 60
        if minutes < 100:
            if seconds < 10:
                add_seconds = "0" + str(seconds)
            else:
                add_seconds = str(seconds)
            possible.append(str(minutes) + add_seconds)
        if seconds < 40:
            minutes -= 1
            possible.append(str(minutes) + str(seconds + 60))
        min_cost = float("inf")
        for combination in possible:
            start = str(startAt)
            curr_cost = i = 0
            while combination[i] == '0':
                i += 1
            for idx in range(i, len(combination)):
                curr_cost += pushCost
                if combination[idx] != start:
                    curr_cost += moveCost
                    start = combination[idx]
            min_cost = min(min_cost, curr_cost)
        return min_cost
