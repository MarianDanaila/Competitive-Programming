class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        i = 0
        index = j = n-1
        out = [0] * n
        while i <= j:
            if abs(nums[i]) >= abs(nums[j]):
                out[index] = nums[i] * nums[i]
                i += 1
            else:
                out[index] = nums[j] * nums[j]
                j -= 1
            index -= 1
        return out
