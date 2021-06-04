from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        squares = [0] * n
        i = 0
        j = n - 1
        index = n - 1
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                squares[index] = nums[i] * nums[i]
                i += 1
            else:
                squares[index] = nums[j] * nums[j]
                j -= 1
            index -= 1

        return squares
