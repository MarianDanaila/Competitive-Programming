class Solution:
    def canFormArray(self, arr, pieces):
        n = len(arr)
        m = len(pieces)
        idx = {}
        for i in range(m):
            for j in range(len(pieces[i])):
                idx[pieces[i][j]] = i

        i = 0
        while i < n:
            search = arr[i]
            if search not in idx:
                return False
            index = idx[search]
            for j in range(len(pieces[index])):
                if search != pieces[index][j]:
                    return False
                else:
                    i += 1
                    if i == n:
                        return True
                    search = arr[i]
        return True
