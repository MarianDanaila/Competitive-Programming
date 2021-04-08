from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        for i in range(n):
            arr[i] %= k
        arr.sort()
        start = -1
        for i in range(n):
            if arr[i] == 0:
                start = i
            else:
                break
        start += 1
        end = n - 1
        if start % 2 != 0:
            return False
        while start < end:
            if arr[start] + arr[end] != k:
                return False
            start += 1
            end -= 1
        return True
