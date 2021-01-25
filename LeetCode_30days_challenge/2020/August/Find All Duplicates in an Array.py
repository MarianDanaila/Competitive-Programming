class Solution:
    def findDuplicates(self, nums):
        output = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                output.append(index+1)
            else:
                nums[index] = -nums[index]
        return output


sol = Solution()
print(sol.findDuplicates([4,3,2,7,8,2,3,1]))
