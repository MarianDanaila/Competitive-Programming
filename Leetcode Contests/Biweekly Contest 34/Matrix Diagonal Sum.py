class Solution:
    def diagonalSum(self, mat) -> int:
        suma = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j:
                    suma += mat[i][j]
                if i+j == len(mat)-1:
                    suma += mat[i][j]
        if len(mat) % 2 == 1:
            suma -= mat[len(mat)//2][len(mat)//2]
        return suma
