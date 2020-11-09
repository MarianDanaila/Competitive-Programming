class Solution:
    def bestTeamScore(self, scores, ages):
        n = len(scores)
        team = []
        for i in range(n):
            team.append([scores[i], ages[i]])
        team.sort(key=lambda x: (-x[1], -x[0]))
        dp = [0] * n
        for i in range(n):
            score = team[i][0]
            dp[i] = score
            for j in range(i):
                if team[j][0] >= team[i][0]:
                    dp[i] = max(dp[i], dp[j]+score)
        return max(dp)
