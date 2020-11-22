class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        string = ['a'] * n
        numeric_value = n
        for i in range(n-1, -1, -1):
            if numeric_value < k:
                string[i] = chr(min(122, k-numeric_value+97))
                numeric_value += ord(string[i])-97
            if numeric_value == k:
                break
        return ''.join(string)
