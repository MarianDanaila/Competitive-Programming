class Solution:
    def angleClock(self, hour, minutes):
        if hour == 12:
            hour = 0
        ans = 6*(abs(minutes-(hour + minutes/60)*5))
        if ans > 180:
            return 360 - ans
        return ans