class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        ans = duration * len(timeSeries)
        for i in range(1, len(timeSeries)):
            ans -= max(0, timeSeries[i-1]+duration-timeSeries[i])
        return ans
