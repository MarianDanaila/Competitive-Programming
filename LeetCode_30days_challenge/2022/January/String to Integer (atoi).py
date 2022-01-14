class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = result = 0
        negative = False
        limit = 2 ** 31
        while i < n and s[i] == ' ':  # jump the white spaces
            i += 1
        if i < n:  # check the sign
            if s[i] == '-':
                negative = True
                i += 1
            elif s[i] == '+':
                i += 1
        # construct the number
        while i < n and '0' <= s[i] <= '9':
            result = result * 10 + ord(s[i]) - 48
            # check for limits
            if negative and result >= limit:
                return -limit
            if not negative and result >= limit - 1:
                return limit - 1
            i += 1
        if negative:
            result *= -1
        return result
