from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        diff = {}
        for num in nums:
            rev = 0
            copy_num = num
            while num > 0:
                rev = rev * 10 + num % 10
                num //= 10
            difference = copy_num-rev
            if difference in diff:
                diff[difference] += 1
            else:
                diff[difference] = 1
        nice_pairs = 0
        for difference in diff:
            nice_pairs += diff[difference] * (diff[difference] - 1) // 2
        return nice_pairs % (10 ** 9 + 7)
