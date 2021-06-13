from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good_triplets = []
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                good_triplets.append([a, b, c])

        max_a = max_b = max_c = 1
        for a, b, c in good_triplets:
            max_a = max(max_a, a)
            max_b = max(max_b, b)
            max_c = max(max_c, c)
        return max_a == target[0] and max_b == target[1] and max_c == target[2]
