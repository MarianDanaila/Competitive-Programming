class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        length = 2 ** (N-2)
        if K > length:
            if K % length != 0:
                K %= length
            return (self.kthGrammar(N-1, K)) ^ 1
        else:
            return self.kthGrammar(N-1, K)
