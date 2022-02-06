class Solution:
    def removeDuplicates(self, nums):
        idx = 0
        same = 1
        n = len(nums)
        for i in range(1, n):
            if nums[idx] != nums[i]:
                same = 1
                idx += 1
                nums[idx] = nums[i]
            else:
                if same < 2:
                    same += 1
                    idx += 1
                    nums[idx] = nums[i]
        return idx + 1
