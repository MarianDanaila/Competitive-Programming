from math import sqrt
from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        n = int((-1 + sqrt(1 + 4 * finalSum)) // 2)
        ans = []
        for i in range(1, n + 1):
            ans.append(2 * i)
        ans_sum = sum(ans)
        if ans_sum != finalSum:
            ans.append(finalSum - ans_sum + ans.pop())

        return ans
