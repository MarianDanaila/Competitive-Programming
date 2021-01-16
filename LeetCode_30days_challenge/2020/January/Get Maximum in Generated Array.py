class Solution:
    def getMaximumGenerated(self, n):
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        maximum = 1
        for i in range(1, n // 2 + 1):
            nums[2 * i] = nums[i]
            if i == n // 2 and n % 2 == 0:
                break
            nums[2 * i + 1] = nums[i] + nums[i + 1]
            maximum = max(maximum, nums[i] + nums[i + 1])
        return maximum
