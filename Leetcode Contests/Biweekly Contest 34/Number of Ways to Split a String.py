class Solution:
    def numWays(self, s: str) -> int:
        ones = 0
        arr = []
        cnt = 0
        flag = True
        p = 1
        modulo = 10 ** 9 + 7
        for ch in s:
            if ch == '1':
                ones += 1
        if ones % 3 != 0:
            return 0
        if ones == 0:
            return ((len(s) - 2) * (len(s) - 1) // 2) % modulo

        if ones == 3:
            for i in range(len(s)):
                if s[i] == '1':
                    arr.append(i)
            for i in range(len(arr) - 1):
                p *= arr[i + 1] - arr[i]
            return p % modulo

        else:
            for i in range(len(s)):
                if s[i] == '1':
                    cnt += 1
                if cnt == ones // 3 and flag:
                    index = i
                    flag = False
                if cnt == ones // 3 + 1:
                    arr.append(i - index)
                    cnt = 1
                    flag = True
            # print(arr)
            for i in arr:
                p *= i
            return p % modulo
