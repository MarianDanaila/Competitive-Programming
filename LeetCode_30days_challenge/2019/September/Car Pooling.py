# Approach 1 using sorting
# Time-complexity: O(N log N)
class Solution:
    def carPooling(self, trips, capacity):
        timestamp = []
        for trip in trips:
            timestamp.append([trip[1], -trip[0]])
            timestamp.append([trip[2], trip[0]])
        timestamp.sort(key=lambda x: (x[0], -x[1]))
        for el in timestamp:
            capacity += el[1]
            if capacity < 0:
                return False
        return True

# Approach 2 using Bucket Sort
# Time-complexity: O(N)
class Solution2:
    def carPooling(self, trips, capacity):
        timestamp = [0] * 1001
        for trip in trips:
            timestamp[trip[1]] -= trip[0]
            timestamp[trip[2]] += trip[0]
        for i in range(1001):
            capacity += timestamp[i]
            if capacity < 0:
                return False
        return True
