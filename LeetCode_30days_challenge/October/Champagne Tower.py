class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        matrix = [[0] * i for i in range(1, 102)]
        matrix[0][0] = poured
        for row in range(query_row + 1):
            for col in range(row + 1):
                add = (matrix[row][col] - 1) / 2
                if add > 0:
                    matrix[row + 1][col] += add
                    matrix[row + 1][col + 1] += add
        return min(1, matrix[query_row][query_glass])
