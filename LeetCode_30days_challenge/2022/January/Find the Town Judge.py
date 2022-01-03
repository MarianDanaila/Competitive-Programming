from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        trusters = set()
        possible_town_judges = {}
        for a, b in trust:
            trusters.add(a)
            if b not in possible_town_judges:
                possible_town_judges[b] = 1
            else:
                possible_town_judges[b] += 1

        for possible_town_judge in possible_town_judges:
            if possible_town_judges[possible_town_judge] == n - 1 and possible_town_judge not in trusters:
                return possible_town_judge
        return -1
