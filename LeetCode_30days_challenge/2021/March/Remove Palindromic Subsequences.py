class Solution:
    def removePalindromeSub(self, s):
        if s == "":
            return 0

        i = 0
        j = len(s) - 1
        palindrome = True
        while i < j:
            if s[i] != s[j]:
                palindrome = False
                break
            i += 1
            j -= 1

        if palindrome:
            return 1
        else:
            return 2
