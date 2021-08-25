from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        prev = None
        not_used = used = 0
        for num in sorted(counter):
            if num - 1 != prev:
                not_used, used = max(not_used, used), counter[num] * num + max(not_used, used)
            else:
                not_used, used = max(not_used, used), counter[num] * num + not_used
            prev = num
        return max(not_used, used)
