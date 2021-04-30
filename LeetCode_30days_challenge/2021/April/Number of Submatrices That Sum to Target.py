class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(1, m):
                matrix[i][j] += matrix[i][j - 1]

        counter = 0
        for col_start in range(m):
            for col_end in range(col_start, m):
                dct = {0: 1}
                curr_sum = 0
                for row in range(n):
                    curr_sum += matrix[row][col_end]
                    if col_start > 0:
                        curr_sum -= matrix[row][col_start - 1]
                    if curr_sum - target in dct:
                        counter += dct[curr_sum - target]
                    if curr_sum in dct:
                        dct[curr_sum] += 1
                    else:
                        dct[curr_sum] = 1
        return counter
