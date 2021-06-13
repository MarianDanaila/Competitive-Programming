from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        n = len(chalk)
        for i in range(n):
            if chalk[i] > k:
                return i
            k -= chalk[i]
