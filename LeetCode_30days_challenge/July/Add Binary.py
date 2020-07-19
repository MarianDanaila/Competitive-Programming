class Solution:
    def addBinary(self, a, b):
        ans = ""
        mind = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 and j >= 0:
            if int(a[i]) + int(b[j]) == 0:
                ans += str(mind)
                mind = 0
            elif int(a[i]) + int(b[j]) == 1:
                ans += str(abs(mind-1))
            else:
                ans += str(mind)
                mind = 1
            i -= 1
            j -= 1

        while i >= 0:
            if a[i] == "0":
                ans += str(mind)
                mind = 0
            else:
                ans += str(abs(mind-1))
            i -= 1

        while j >= 0:
            if b[j] == "0":
                ans += str(mind)
                mind = 0
            else:
                ans += str(abs(mind-1))
            j -= 1

        if mind == 1:
            ans += str(mind)

        return ans[::-1]



sol = Solution()
print(sol.addBinary("11", "1"))
