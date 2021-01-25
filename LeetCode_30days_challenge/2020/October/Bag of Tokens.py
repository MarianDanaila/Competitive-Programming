class Solution:
    def bagOfTokensScore(self, tokens, P):
        tokens.sort()
        max_score = score = 0
        i = 0
        j = len(tokens)-1
        while i <= j:
            if P >= tokens[i]:
                score += 1
                P -= tokens[i]
                i += 1
            else:
                if score > 0:
                    score -= 1
                    P += tokens[j]
                j -= 1
            max_score = max(max_score, score)
        return max_score
