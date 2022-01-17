class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev_seat = None
        n = len(seats)
        max_distance = 1
        for i in range(n):
            if seats[i] == 1:
                if prev_seat is None:
                    max_distance = max(max_distance, i)
                else:
                    max_distance = max(max_distance, (i - prev_seat) // 2)
                prev_seat = i
        return max(max_distance, n - 1 - prev_seat)
