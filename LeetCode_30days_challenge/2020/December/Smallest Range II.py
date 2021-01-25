class Solution:
    def smallestRangeII(self, A, K: int) -> int:
        A.sort()
        min_a = A[0]
        max_a = A[-1]
        ans = max_a-min_a
        min_a += K
        max_a -= K
        if min_a > max_a:
            min_a, max_a = max_a, min_a
        for i in range(len(A)-1):
            ans = min(ans, max(max_a, A[i]+K)-min(min_a, A[i+1]-K))
        return ans
