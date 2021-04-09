from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if left:
            max_left = max(left)
        else:
            max_left = -1
        if right:
            min_right = min(right)
        else:
            min_right = n
        return max(n-min_right, max_left)
