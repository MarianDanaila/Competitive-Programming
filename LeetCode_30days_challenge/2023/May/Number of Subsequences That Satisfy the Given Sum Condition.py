from typing import List

# Solution1: Using sorting + binary search
class Solution1:
    def numSubseq(self, nums: List[int], target: int) -> int:
        def binary_search(low, high, target):
            idx = low
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
                    idx = mid
            return idx

        nums.sort()
        n = len(nums)
        subsequences = 0
        for i in range(n):
            if 2 * nums[i] > target:
                return subsequences % (10 ** 9 + 7)
            idx = binary_search(i, n - 1, target - nums[i])
            subsequences += 2 ** (idx - i)
        return subsequences % (10 ** 9 + 7)


# Solution2: Using sorting + two pointers technique
class Solution2:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        subsequences = 0
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] + nums[end] <= target:
                subsequences += 2 ** (end - start)
                start += 1
            else:
                end -= 1
        return subsequences % (10 ** 9 + 7)
