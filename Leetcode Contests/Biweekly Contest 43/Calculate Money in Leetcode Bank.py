class Solution:
    def totalMoney(self, n: int) -> int:
        monday = day = 1
        total = 0
        for i in range(1, n+1):
            if i % 7 == 1:
                total += monday
                monday += 1
                day = monday
            else:
                total += day
                day += 1
        return total
