from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        n = len(nums)
        for i in range(n - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                low, high, target = i + 1, n - 1, -nums[i]
                while low < high:
                    if nums[low] + nums[high] == target:
                        triplets.append([nums[i], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < target:
                        low += 1
                    else:
                        high -= 1

        return triplets
