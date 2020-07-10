class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        column = m
        for row in range(n):
            i = 0
            j = column - 1
            while i <= j:
                mid = i + (j - i) // 2
                if binaryMatrix.get(row, mid) == 1:
                    j = mid - 1
                    column = mid
                    if column == 0:
                        return 0

                else:
                    i = mid + 1
        if column == m:
            return -1
        else:
            return column
