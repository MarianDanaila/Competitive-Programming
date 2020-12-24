class Solution:
    def nextGreaterElement(self, n: int) -> int:
        str_n = str(n)
        index = -1
        for i in range(len(str_n) - 1, 0, -1):
            if str_n[i] > str_n[i - 1]:
                value = str_n[i - 1]
                index = i - 1
                break
        if index == -1:
            return -1

        digits = [0] * 10
        for i in range(index + 1, len(str_n)):
            digits[int(str_n[i])] += 1
        ans = 0
        for i in range(len(str_n) - 1, 0, -1):
            if str_n[i] > value:
                keep = i
                digits[int(str_n[i])] -= 1
                break

        for i in range(index + 1):
            if i == index:
                ans = ans * 10 + int(str_n[keep])
                digits[int(str_n[i])] += 1
            else:
                ans = ans * 10 + int(str_n[i])
        for i in range(10):
            while digits[i] > 0:
                digits[i] -= 1
                ans = ans * 10 + i
        if ans > 2 ** 31 - 1:
            return -1
        else:
            return ans
