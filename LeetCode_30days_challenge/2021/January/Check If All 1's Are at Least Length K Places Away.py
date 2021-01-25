class Solution:
    def kLengthApart(self, nums, k: int) -> bool:
        prev = -k - 1
        for i in range(len(nums)):
            if nums[i] == 1:
                if i - prev - 1 < k:
                    return False
                prev = i

        return True
