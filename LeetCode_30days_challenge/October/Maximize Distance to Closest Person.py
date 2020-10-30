class Solution:
    def maxDistToClosest(self, seats):
        n = len(seats)
        max_distance = 0
        first = True
        for i in range(n):
            if seats[i] == 1:
                if first:
                    max_distance = i
                    first = False
                else:
                    max_distance = max(max_distance, (i - start) // 2)
                start = i
        max_distance = max(max_distance, n - 1 - start)
        return max_distance
