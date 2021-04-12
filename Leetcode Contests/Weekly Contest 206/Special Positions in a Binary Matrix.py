from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        counter = 0
        for i in range(n):
            cnt = 0
            for j in range(m):
                if mat[i][j] == 1:
                    col = j
                    cnt += 1
            if cnt == 1:
                cnt = 0
                for row in range(n):
                    if mat[row][col] == 1:
                        cnt += 1
                if cnt == 1:
                    counter += 1
        return counter
