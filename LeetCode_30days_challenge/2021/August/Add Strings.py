class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len1, len2 = len(num1), len(num2)
        idx1, idx2 = len1 - 1, len2 - 1
        one = 0
        sum_num = []
        while idx1 >= 0 and idx2 >= 0:
            sum_digits = int(num1[idx1]) + int(num2[idx2]) + one
            sum_num.append(sum_digits % 10)
            one = sum_digits // 10
            idx1 -= 1
            idx2 -= 1

        while idx1 >= 0:
            sum_digits = int(num1[idx1]) + one
            sum_num.append(sum_digits % 10)
            one = sum_digits // 10
            idx1 -= 1

        while idx2 >= 0:
            sum_digits = int(num2[idx2]) + one
            sum_num.append(sum_digits % 10)
            one = sum_digits // 10
            idx2 -= 1

        if one:
            sum_num.append(1)
        return "".join(map(str, sum_num[::-1]))
