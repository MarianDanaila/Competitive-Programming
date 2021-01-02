class Solution:
    def search(self, nums, target):
        return self.helper(nums, target, 0, len(nums) - 1)

    def helper(self, nums, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] == nums[mid]:
            left += 1
        elif nums[left] < nums[mid]:
            if nums[mid] > target >= nums[left]:
                return self.helper(nums, target, left, mid - 1)
            else:
                return self.helper(nums, target, mid + 1, right)
        else:
            if nums[mid] < target <= nums[right]:
                return self.helper(nums, target, mid + 1, right)
            else:
                return self.helper(nums, target, left, mid - 1)
