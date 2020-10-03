class Solution:
    def minSubarray(self, nums, p):
        target = sum(nums) % p
        if target == 0:
            return 0
        dp = {0: -1}
        cur = 0
        res = len(nums)
        for i in range(len(nums)):
            cur = (cur+nums[i]) % p
            dp[cur] = i
            if (cur-target) % p in dp:
                res = min(res, i-dp[(cur-target) % p])
        if res == len(nums):
            return -1
        else:
            return res
