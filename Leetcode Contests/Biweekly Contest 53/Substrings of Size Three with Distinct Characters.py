class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n - 2):
            substring = s[i:i + 3]
            characters = set()
            good = True
            for ch in substring:
                if ch not in characters:
                    characters.add(ch)
                else:
                    good = False
                    break
            if good:
                ans += 1
        return ans
