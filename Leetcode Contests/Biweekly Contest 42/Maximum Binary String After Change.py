class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        zero = 0
        first = True
        for i in range(len(binary)):
            if binary[i] == '0':
                if first:
                    first = False
                    idx1 = i
                else:
                    idx2 = i
                zero += 1
        if zero < 2:
            return binary
        one = 0
        for i in range(idx1, idx2 + 1):
            if binary[i] == '1':
                one += 1
        last_zero = idx2 - one
        ans = '1' * last_zero + '0' + (len(binary) - 1 - last_zero) * '1'
        return ans
