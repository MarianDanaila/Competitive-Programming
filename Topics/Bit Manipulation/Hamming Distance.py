# Approach 1: Just check every bit in both numbers and increment when they are different
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming_distance = 0
        while x != 0 or y != 0:
            if x % 2 != y % 2:
                hamming_distance += 1
            x = x >> 1
            y = y >> 1
        return hamming_distance


# Approach 2: Just make XOR of x and y and after that count the number of '1' bits.
# because XOR of two different bits is always 1
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming_distance = 0
        new = x ^ y
        while new > 0:
            if new % 2 == 1:
                hamming_distance += 1
            new = new >> 1
        return hamming_distance


# Approach 3: Again make XOR of x and y but when we count the number of '1' bits
# we make the trick n&(n-1) which removes last '1' bit
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming_distance = 0
        new = x ^ y
        while new > 0:
            new = new & (new-1)
            hamming_distance += 1
        return hamming_distance
