class Solution:
    def findComplement(self, num: int) -> int:
        binary = []
        while num > 0:
            binary.append(num % 2)
            num //= 2

        complement = 0
        binary_length = len(binary)
        for i in range(binary_length - 1, -1, -1):
            complement = complement * 2 + abs(binary[i] - 1)
        return complement
