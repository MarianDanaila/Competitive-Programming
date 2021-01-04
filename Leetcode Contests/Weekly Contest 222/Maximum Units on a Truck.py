class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        size = 0
        units = 0
        n = len(boxTypes)
        for i in range(n):
            units += min(truckSize - size, boxTypes[i][0]) * boxTypes[i][1]
            size += boxTypes[i][0]
            if size >= truckSize:
                break
        return units
