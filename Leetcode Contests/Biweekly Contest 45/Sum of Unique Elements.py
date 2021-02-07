from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        total = 0
        for key in counter:
            if counter[key] == 1:
                total += key
        return total
