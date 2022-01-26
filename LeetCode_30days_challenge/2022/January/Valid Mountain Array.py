from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        idx = 1
        while idx < n and arr[idx] > arr[idx - 1]:
            idx += 1
        peak = idx - 1
        while idx < n:
            if arr[idx] >= arr[idx - 1]:
                return False
            idx += 1
        return 0 < peak < n - 1