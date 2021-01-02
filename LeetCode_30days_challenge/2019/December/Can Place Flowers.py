class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        length = len(flowerbed)
        start = -1
        for i in range(length):
            if flowerbed[i] == 1:
                start = i
                n -= i // 2
                if n <= 0:
                    return True
                break
        if start == -1:
            return n <= (length + 1) // 2
        for i in range(length - 1, start - 1, -1):
            if flowerbed[i] == 1:
                end = i
                n -= (length - 1 - i) // 2
                if n <= 0:
                    return True
                break
        for i in range(start + 1, end + 1):
            if flowerbed[i] == 1:
                n -= (i - start - 2) // 2
                start = i
                if n <= 0:
                    return True
        return False
