class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        strings = ['0']
        index = 1

        while index < n:
            invert = ""
            s = ""
            for ch in strings[-1]:
                if ch == '0':
                    invert += '1'
                else:
                    invert += '0'
            strings.append(strings[-1] + "1" + invert[::-1])
            index += 1
        # print(strings)
        return strings[-1][k - 1]
