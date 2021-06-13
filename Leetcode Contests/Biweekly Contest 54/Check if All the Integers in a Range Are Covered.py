from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            good = False
            for start, end in ranges:
                if start <= i <= end:
                    good = True
                    break
            if not good:
                return False
        return True
