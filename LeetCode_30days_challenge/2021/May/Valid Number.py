class Solution:
    def isNumber(self, s: str) -> bool:
        dot = e = digit = 0
        sign = True
        for ch in s:
            if ch == '+' or ch == '-':
                if not sign:
                    return False
            elif '0' <= ch <= '9':
                digit += 1
            elif ch == '.':
                dot += 1
                if dot == 2 or e > 0:
                    return False
            elif ch == 'e' or ch == 'E':
                e += 1
                if digit == 0 or e > 1:
                    return False
                sign = True
                digit = 0
                continue
            else:
                return False

            sign = False

        return digit > 0
