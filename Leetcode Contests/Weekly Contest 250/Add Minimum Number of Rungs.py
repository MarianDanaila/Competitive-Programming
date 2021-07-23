from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        n = len(rungs)
        counter = rungs[0] // dist
        if rungs[0] % dist == 0:
            counter -= 1
        for i in range(1, n):
            counter += (rungs[i] - rungs[i - 1]) // dist
            if (rungs[i] - rungs[i - 1]) % dist == 0:
                counter -= 1

        return counter
