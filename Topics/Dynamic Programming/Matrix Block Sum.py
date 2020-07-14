class Solution:
    def matrixBlockSum(self, mat, k: int):
        ans = [[0] * len(mat[0]) for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == 0 and j == 0:
                    mat[i][j] = mat[0][0]
                elif i == 0:
                    mat[i][j] += mat[i][j - 1]
                elif j == 0:
                    mat[i][j] += mat[i - 1][j]
                else:
                    mat[i][j] += mat[i][j - 1] + mat[i - 1][j] - mat[i - 1][j - 1]

        for i in range(len(ans)):
            lower_row = max(0, i - k)
            upper_row = min(i + k, len(ans) - 1)
            for j in range(len(ans[0])):
                lower_col = max(0, j - k)
                upper_col = min(j + k, len(ans[0]) - 1)
                if lower_col == 0 and lower_row == 0:
                    ans[i][j] = mat[upper_row][upper_col]
                elif lower_col == 0:
                    ans[i][j] = mat[upper_row][upper_col] - mat[lower_row - 1][upper_col]
                elif lower_row == 0:
                    ans[i][j] = mat[upper_row][upper_col] - mat[upper_row][lower_col - 1]
                else:
                    ans[i][j] = mat[upper_row][upper_col] - mat[lower_row - 1][upper_col] - mat[upper_row][
                        lower_col - 1] + mat[lower_row - 1][lower_col - 1]

        return ans

