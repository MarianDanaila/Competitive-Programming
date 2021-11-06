from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        mask = xor & (-xor)
        first = second = 0
        for num in nums:
            if mask & num:
                first ^= num
            else:
                second ^= num
        return [first, second]
