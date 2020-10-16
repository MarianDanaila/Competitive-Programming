class Solution:
    def searchMatrix(self, matrix, target):

        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False

        up_row = 0
        down_row = len(matrix) - 1
        while up_row <= down_row:
            mid_row = up_row + (down_row - up_row) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                left_col = 0
                right_col = len(matrix[0]) - 1
                while left_col <= right_col:
                    mid_col = left_col + (right_col - left_col) // 2
                    if matrix[mid_row][mid_col] == target:
                        return True
                    elif matrix[mid_row][mid_col] < target:
                        left_col = mid_col + 1
                    else:
                        right_col = mid_col - 1
                return False
            elif target < matrix[mid_row][0]:
                down_row = mid_row - 1
            else:
                up_row = mid_row + 1
        return False
