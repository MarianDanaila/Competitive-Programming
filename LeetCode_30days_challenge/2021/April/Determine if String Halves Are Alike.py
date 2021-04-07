class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        cnt = 0
        vowels = "aeiouAEIOU"
        n = len(s)
        for i in range(n // 2):
            if s[i] in vowels:
                cnt += 1

        for i in range(n // 2, n):
            if s[i] in vowels:
                cnt -= 1
                if cnt < 0:
                    return False

        return cnt == 0
