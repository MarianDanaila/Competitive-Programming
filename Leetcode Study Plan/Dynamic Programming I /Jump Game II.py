class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = curr_end = curr_farthest = 0
        n = len(nums)
        for i in range(n - 1):
            curr_farthest = max(curr_farthest, i + nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = curr_farthest
                if curr_end >= n - 1:
                    break
        return jumps
