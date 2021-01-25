class Solution:
    def flipAndInvertImage(self, A):
        n = len(A)
        m = len(A[0])

        for i in range(n):
            for j in range(m // 2):
                A[i][j], A[i][m - j - 1] = A[i][m - j - 1], A[i][j]
                if A[i][j] == 1:
                    A[i][j] = 0
                else:
                    A[i][j] = 1

                if A[i][m - j - 1] == 1:
                    A[i][m - j - 1] = 0
                else:
                    A[i][m - j - 1] = 1
            if m % 2 == 1:
                if A[i][m // 2] == 1:
                    A[i][m // 2] = 0
                else:
                    A[i][m // 2] = 1
        return A


# Another solution using XOR
class Solution:
    def flipAndInvertImage(self, A):
        n = len(A)
        m = len(A[0])

        for i in range(n):
            for j in range(m // 2):
                A[i][j], A[i][m - j - 1] = A[i][m - j - 1], A[i][j]
                A[i][j] ^= 1
                A[i][m - j - 1] ^= 1
            if m % 2 == 1:
                A[i][m // 2] ^= 1
        return A
