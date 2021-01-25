class Solution:
    def fourSumCount(self, A, B, C, D):
        n = len(A)
        cnt = 0
        pairs = {}
        for i in range(n):
            for j in range(n):
                pair_sum = A[i] + B[j]
                if pair_sum in pairs:
                    pairs[pair_sum] += 1
                else:
                    pairs[pair_sum] = 1

        for i in range(n):
            for j in range(n):
                pair_sum = C[i] + D[j]
                if -pair_sum in pairs:
                    cnt += pairs[-pair_sum]

        return cnt
