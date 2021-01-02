class Solution:
    def bitwiseComplement(self, N: int) -> int:
        int_n = 0
        binary_n = bin(N)
        for i in range(2, len(binary_n)):
            int_n *= 2
            if int(binary_n[i]) % 2 == 0:
                int_n += 1
        return int_n


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary_n = bin(N)
        s = 2 ** (len(binary_n)-2)-1
        return s-N
