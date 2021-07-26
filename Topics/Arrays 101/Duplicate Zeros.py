from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros = 0
        i = 0
        while zeros < n - i - 1:
            if arr[i] == 0:
                zeros += 1
            i += 1

        if zeros == n - i - 1 and arr[i] == 0:
            arr[i + zeros] = 0
            i -= 1
        elif zeros > n - i - 1:
            i -= 1

        while i >= 0:
            if arr[i] == 0:
                arr[i + zeros] = 0
                zeros -= 1
                arr[i + zeros] = 0
            else:
                arr[i + zeros] = arr[i]
            i -= 1
