class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        index = 1
        curr = []
        for i in range(n):
            if i % 2 == 0:
                curr.append('a')
            else:
                curr.append('b')
        curr = "".join(curr)

        while index < k:
            next_curr = [''] * n
            ch = ''
            for i in range(n - 1, 0, -1):
                if curr[i] == 'a':
                    if curr[i - 1] == 'c':
                        ch = 'b'
                        break
                    else:
                        ch = 'c'
                        break
                elif curr[i] == 'b':
                    if curr[i - 1] == 'a':
                        ch = 'c'
                        break
            if ch == '':
                if curr[0] == 'c':
                    return ""
                else:
                    ch = chr(ord(curr[0]) + 1)
                    next_curr[0] = ch
                    i -= 1
                    i = max(0, i)
            else:
                next_curr[i] = ch
            for j in range(i):
                next_curr[j] = curr[j]
            for j in range(i + 1, n):
                if next_curr[j - 1] == 'a':
                    next_curr[j] = 'b'
                else:
                    next_curr[j] = 'a'
            curr = "".join(next_curr)
            index += 1

        return curr
