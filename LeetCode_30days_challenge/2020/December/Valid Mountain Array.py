class Solution:
    def validMountainArray(self, arr):
        n = len(arr)
        if n < 3:
            return False
        index = -1
        increase = False
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                return False
            elif arr[i] < arr[i-1]:
                index = i
                break
            increase = True
        if index == -1 or not increase:
            return False
        for i in range(index, n):
            if arr[i] >= arr[i-1]:
                return False
        return True
