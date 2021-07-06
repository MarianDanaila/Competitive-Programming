from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        counter = Counter(arr)
        buckets = [[] for _ in range(10 ** 5)]
        set_size = removed = 0
        for integer in counter:
            buckets[counter[integer] - 1].append(integer)
        for i in range(10 ** 5 - 1, -1, -1):
            for _ in range(len(buckets[i])):
                set_size += 1
                removed += i + 1
                if removed >= n // 2:
                    return set_size
