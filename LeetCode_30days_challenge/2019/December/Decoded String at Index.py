class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        length = 0
        for ch in S:
            if 'a' <= ch <= 'z':
                length += 1
            else:
                length *= int(ch)

        for i in range(len(S) - 1, -1, -1):
            K %= length
            if K == 0 and 'a' <= S[i] <= 'z':
                return S[i]

            if 'a' <= S[i] <= 'z':
                length -= 1
            else:
                length //= int(S[i])
