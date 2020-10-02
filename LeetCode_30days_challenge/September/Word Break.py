class Solution:
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for word in wordDict:
                if word == s[i-len(word):i] and dp[i-len(word)]:
                    dp[i] = True
        return dp[-1]
