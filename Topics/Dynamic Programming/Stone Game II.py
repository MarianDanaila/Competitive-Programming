class Solution:
    def stoneGameII(self, piles):
        N = len(piles)
        cache = [[0] * (N+1) for _ in range(N+1)]
        hasCache = [[False] * (N+1) for _ in range(N)]
        def getMax(index, M):
            if index == N:
                return 0
            if hasCache[index][M]:
                return cache[index][M]
            # index -> 0 to N
            # M -> 0 to N
            # the number of possible inputs is O(N^2)
            # time complexity = the number of states * the work per state
            # O(N^2) * O(N^2) = O(N^4)
            best = -float("inf")
            # each state -> O(M^2) work
            for X in range(1, 2 * M + 1):
                stones = sum(piles[index:index+X])
                score = stones - getMax(min(index + X, N), min(max(M, X), N))
                best = max(best, score)

            hasCache[index][M] = True
            cache[index][M] = best
            return best
        # total = myscore + opp's score
        # delta = myscore - opp's score
        # total + delta = myscore * 2

        total = sum(piles)
        delta = getMax(0, 1)
        return (total + delta) // 2
