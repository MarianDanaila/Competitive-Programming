# Approach 1 using Another Array
class Solution:
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        positions = [True]*(len(nums))
        for num in nums:
            if 0 < num <= len(nums):
                positions[num-1] = False
        for i in range(len(positions)):
            if positions[i]:
                return i+1
        return len(nums)+1


# Approach 2 using Set
class Solution:
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        positions = set()
        for i in range(len(nums)):
            positions.add(i + 1)
        for num in nums:
            try:
                if 0 < num <= len(nums):
                    positions.remove(num)
            except KeyError:
                continue
        if len(positions) == 0:
            return len(nums) + 1
        for position in positions:
            return position


# Approach 3 without using Extra Memory
class Solution:
    def firstMissingPositive(self, nums):
        nums.append(0)
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0

        for i in range(n):
            nums[nums[i] % n] += n

        for i in range(1, n):
            if nums[i] // n == 0:
                return i
        return n
