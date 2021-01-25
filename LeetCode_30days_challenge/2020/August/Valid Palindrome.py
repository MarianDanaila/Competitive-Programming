class Solution:
    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
            elif s[i].isalnum():
                j -= 1
            elif s[j].isalnum():
                i += 1
            else:
                i += 1
                j -= 1
        return True
sol = Solution()
print(sol.isPalindrome("1P"))