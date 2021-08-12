from collections import Counter
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        for key in sorted(counter.keys()):
            if counter[key] > 0:
                if key < 0:
                    if key / 2 in counter and counter[key] <= counter[key / 2]:
                        counter[key / 2] -= counter[key]
                    else:
                        return False

                else:
                    if key * 2 in counter and counter[key] <= counter[key * 2]:
                        counter[key * 2] -= counter[key]
                    else:
                        return False
        return True
