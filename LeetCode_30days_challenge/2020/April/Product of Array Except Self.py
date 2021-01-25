# Approach 1 with 2 arrays left and right
# left[i] - what is in the left of i-th element
# right[i] - what is in the right of i-th element
class Solution:
    def productExceptSelf(self, nums):
        output = []
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
            right[len(nums)-i-1] = right[len(nums)-i] * nums[len(nums)-i]
        for i in range(len(nums)):
            output.append(left[i]*right[i])

        return output


