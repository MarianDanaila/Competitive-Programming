class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        counter = 0
        zero_one = True
        if s[0] == '1':
            zero_one = False

        zeros = ones = 0
        n = len(s)

        for i in range(n):
            if not zero_one:
                if s[i] == '0':
                    zeros += 1
                else:
                    zero_one = True
                    counter += min(zeros, ones)
                    ones = 1
            else:
                if s[i] == '1':
                    ones += 1
                else:
                    zero_one = False
                    counter += min(zeros, ones)
                    zeros = 1

        counter += min(zeros, ones)
        return counter
