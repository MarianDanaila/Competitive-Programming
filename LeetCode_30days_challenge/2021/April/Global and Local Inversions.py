from typing import List


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        n = len(A)
        maxim = -1
        for i in range(n-2):
            maxim = max(maxim, A[i])
            if maxim > A[i+2]:
                return False
        return True
