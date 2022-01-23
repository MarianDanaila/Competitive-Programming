from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        start_nr = 12
        digit = 3
        add = 11
        while start_nr <= high:
            nr = start_nr
            while nr % 10 != 0:
                if low <= nr <= high:
                    ans.append(nr)
                nr += add
            start_nr = start_nr * 10 + digit
            add = add * 10 + 1
            digit += 1
        return ans
