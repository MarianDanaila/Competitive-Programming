class Solution:
    def minCostToMoveChips(self, position):
        odd_position = even_position = 0
        for pos in position:
            if pos % 2 == 0:
                even_position += 1
            else:
                odd_position += 1
        return min(even_position, odd_position)
