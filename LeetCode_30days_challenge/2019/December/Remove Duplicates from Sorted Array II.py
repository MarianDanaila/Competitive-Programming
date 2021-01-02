# Approach 1
# Time Complexity: O(N^2) where N is length of the array
class Solution:
    def removeDuplicates(self, nums):
        deleted = 0
        n = len(nums)
        cnt = 1
        for i in range(1, n):
            if nums[i-deleted] == nums[i-deleted-1]:
                cnt += 1
                if cnt > 2:
                    nums.pop(i-deleted)
                    deleted += 1
            else:
                cnt = 1
        return len(nums)

# Approach 2
# Time Complexity: O(N) where N is length of the array


class Solution2:
    def removeDuplicates(self, nums):
        i = 0
        for num in nums:
            if i < 2 or num > nums[i-2]:
                nums[i] = num
                i += 1
        return i
