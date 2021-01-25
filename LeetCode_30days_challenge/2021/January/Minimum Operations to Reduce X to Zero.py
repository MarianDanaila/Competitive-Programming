class Solution:
    def minOperations(self, nums, x):
        target = sum(nums) - x
        sums = {0: -1}
        acc_sum = 0
        max_length = 0
        for i in range(len(nums)):
            acc_sum += nums[i]
            if acc_sum - target in sums:
                max_length = max(max_length, i - sums[acc_sum - target])
            else:
                sums[acc_sum] = i

        if max_length == 0 and target != 0:
            return -1
        return len(nums) - max_length
