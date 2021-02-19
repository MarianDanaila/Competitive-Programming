from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        slices = cnt = 0
        r = A[1]-A[0]
        for i in range(2, n):
            if A[i]-A[i-1] == r:
                cnt += 1
                slices += cnt
            else:
                r = A[i]-A[i-1]
                cnt = 0
        return slices
