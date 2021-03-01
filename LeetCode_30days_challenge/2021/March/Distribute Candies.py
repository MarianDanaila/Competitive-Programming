from collections import Counter
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        counter = Counter(candyType)
        n = len(candyType)
        return min(len(counter), n//2)
