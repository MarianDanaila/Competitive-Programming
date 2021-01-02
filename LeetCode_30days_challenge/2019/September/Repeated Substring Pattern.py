class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) < 2:
            return False
        n = len(s)
        i = n // 2

        while i > 0:
            if n % i == 0:  # if it is divisor then check all substring of length i
                index = 0
                equal = True
                for _ in range(n // i - 1):

                    if s[index:index + i] != s[index + i:index + i + i]:
                        equal = False
                        break
                    index = index + i
                if equal:
                    return True
            i -= 1
        return False


