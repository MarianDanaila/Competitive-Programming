class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = len(flowerbed)
        if n == 0:
            return True
        if flowers == 1 and flowerbed[0] == 0:
            n -= 1
            return n == 0
        i = 0
        while i < flowers:
            if flowerbed[i] == 0:
                if (i == 0 and flowerbed[i + 1] == 0) or (i == flowers - 1 and flowerbed[i - 1] == 0) or (
                        flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    i += 1
                    n -= 1
                    if n == 0:
                        return True
            i += 1
        return n == 0
