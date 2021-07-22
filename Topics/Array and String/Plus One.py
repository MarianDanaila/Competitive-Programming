from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        idx = n - 1
        while digits[idx] == 9:
            digits[idx] = 0
            idx -= 1
            if idx == -1:
                digits.insert(0, 1)
                return digits
        digits[idx] += 1
        return digits
