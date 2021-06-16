from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        total_units = 0
        for boxes, units in boxTypes:
            if boxes < truckSize:
                truckSize -= boxes
                total_units += boxes * units
            else:
                total_units += truckSize * units
                break
        return total_units
