class Solution:
    def eraseOverlapIntervals(self, intervals):
        end = -float("inf")
        counter = 0
        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        for interval in sorted_intervals:
            if interval[0] < end:
                counter += 1
            else:
                end = interval[1]
        return counter
