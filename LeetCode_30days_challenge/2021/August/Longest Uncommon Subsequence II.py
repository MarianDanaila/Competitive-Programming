from itertools import combinations
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        subsequences = {}

        def all_subsequences(s):
            for r in range(1, len(s) + 1):
                for c in combinations(s, r):
                    subsequence = "".join(c)
                    if subsequence in subsequences:
                        subsequences[subsequence] += 1
                    else:
                        subsequences[subsequence] = 1

        for string in strs:
            all_subsequences(string)

        longest = -1
        for subsequence in subsequences:
            if subsequences[subsequence] == 1:
                longest = max(longest, len(subsequence))
        return longest
