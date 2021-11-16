class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(x):
            counter = 0
            for i in range(m):
                counter += min(x // i, n)
            return counter

        low, high = 1, m * n
        while low < high:
            mid = low + (high - low) // 2
            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return high
