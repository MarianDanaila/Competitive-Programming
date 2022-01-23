class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = 0
        n = len(corridor)
        start_division = -1
        ways = 1
        enough_seats = False
        for i in range(n):
            if corridor[i] == 'S':
                seats += 1
                if seats == 1:
                    if start_division != -1:
                        ways *= (i - start_division)
                        start_divison = -1
                elif seats == 2:
                    enough_seats = True
                    seats = 0
                    start_division = i
        if not enough_seats or seats == 1:
            return 0
        return ways % (10 ** 9 + 7)
