class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total_prod = 0
        len1, len2 = len(num1), len(num2)
        for i in range(len1 - 1, -1, -1):
            curr_prod = add = 0
            power = len1 - i - 1
            for j in range(len2 - 1, -1, -1):
                prod_of_digits = (ord(num2[j]) - 48) * (ord(num1[i]) - 48) + add
                curr_prod += prod_of_digits % 10 * (10 ** power)
                add = prod_of_digits // 10
                power += 1
            curr_prod += add % 10 * (10 ** power)
            total_prod += curr_prod
        return str(total_prod)
