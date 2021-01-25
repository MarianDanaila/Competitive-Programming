class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return
        if len(nums) == 1:
            return [str(nums[0])]
        out = []
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] - nums[j - 1] != 1:
                if i == j - 1:
                    out.append(str(nums[i]))
                else:
                    out.append(str(nums[i]) + '->' + str(nums[j - 1]))
                i = j
            j += 1
        if i == j - 1:
            out.append(str(nums[i]))
        else:
            out.append(str(nums[i]) + '->' + str(nums[j - 1]))

        return out
