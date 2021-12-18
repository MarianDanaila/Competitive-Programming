from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        nr_digits = len(digits)
        str_n = str(n)
        len_n = len(str_n)
        if int(digits[0] * len_n) > n:
            if nr_digits > 1:
                return nr_digits * (nr_digits ** (len_n - 1) - 1) // (nr_digits - 1)
            return len_n - 1
        else:
            # binary search
            if nr_digits > 1:
                total = nr_digits * (nr_digits ** (len_n - 1) - 1) // (nr_digits - 1)
            else:
                total = len_n - 1
            for i in range(len_n):
                low, high = 0, nr_digits - 1
                idx = -1
                while low <= high:
                    mid = low + (high - low) // 2
                    if digits[mid] <= str_n[i]:
                        idx = mid
                        low = mid + 1
                    else:
                        high = mid - 1
                if digits[idx] == str_n[i]:
                    total += idx * (nr_digits ** (len_n - i - 1))
                    if i == len_n - 1:
                        total += 1
                else:
                    total += (idx + 1) * (nr_digits ** (len_n - i - 1))
                    break
            return total
