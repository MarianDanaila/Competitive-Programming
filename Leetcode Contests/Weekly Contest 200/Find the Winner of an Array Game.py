class Solution:
    def getWinner(self, arr, k):
        wins = {}
        for i in arr:
            wins[i] = 0
        while True:
            if arr[0] < arr[1]:
                arr[0], arr[1] = arr[1], arr[0]
            wins[arr[0]] += 1
            if wins[arr[0]] == k:
                return arr[0]
            elif wins[arr[0]] == len(arr) - 1:
                return arr[0]
            arr.pop(1)
            arr.append(arr[1])
