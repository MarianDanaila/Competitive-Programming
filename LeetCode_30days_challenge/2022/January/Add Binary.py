class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        min_length = min(len(a), len(b))
        i = -1
        keep = 0
        while i > -min_length - 1:
            bit_a = ord(a[i]) - 48
            bit_b = ord(b[i]) - 48
            result.append((bit_a + bit_b + keep) % 2)
            keep = (bit_a + bit_b + keep) // 2
            i -= 1
        while i > -len(a) - 1:
            bit_a = ord(a[i]) - 48
            result.append((bit_a + keep) % 2)
            keep = (bit_a + keep) // 2
            i -= 1
        while i > -len(b) - 1:
            bit_b = ord(b[i]) - 48
            result.append((bit_b + keep) % 2)
            keep = (bit_b + keep) // 2
            i -= 1

        if keep > 0:
            result.append(1)
        return "".join(map(str, result[::-1]))
