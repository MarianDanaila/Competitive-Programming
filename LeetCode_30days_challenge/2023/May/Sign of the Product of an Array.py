from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        """
        1 - meaning positive
        -1 - meaning negative
        """
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign *= -1
        return sign
