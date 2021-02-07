from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        negative_sum = positive_sum = total_negative_sum = total_positive_sum = 0
        for num in nums:
            negative_sum += num
            positive_sum += num
            if positive_sum < 0:
                positive_sum = 0
            else:
                total_positive_sum = max(total_positive_sum, positive_sum)

            if negative_sum > 0:
                negative_sum = 0
            else:
                total_negative_sum = min(total_negative_sum, negative_sum)

        return max(total_positive_sum, -total_negative_sum)
