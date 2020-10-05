class Solution:
    def maxProductPath(self, arr):
        n = len(arr)
        m = len(arr[0])
        min_path = [[0] * m for _ in range(n)]
        max_path = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                min_value = float("inf")
                max_value = -float("inf")
                if i == 0 and j == 0:
                    min_value = arr[i][j]
                    max_value = arr[i][j]
                if i > 0:
                    temp_max = max(arr[i][j] * min_path[i-1][j], arr[i][j] * max_path[i-1][j])
                    max_value = max(temp_max, max_value)

                    temp_min = min(arr[i][j] * min_path[i-1][j], arr[i][j] * max_path[i-1][j])
                    min_value = min(temp_min, min_value)

                if j > 0:
                    temp_max = max(arr[i][j] * min_path[i][j-1], arr[i][j] * max_path[i][j-1])
                    max_value = max(temp_max, max_value)

                    temp_min = min(arr[i][j] * min_path[i][j-1], arr[i][j] * max_path[i][j-1])
                    min_value = min(temp_min, min_value)

                min_path[i][j] = min_value
                max_path[i][j] = max_value

        if max_path[-1][-1] < 0:
            return -1
        else:
            return max_path[-1][-1]
