class Solution:
    def minimumSum(self, num: int) -> int:
        digits = [num // 1000 % 10, num // 100 % 10, num // 10 % 10, num % 10]
        min_sum = float("inf")
        for i in range(3):
            for j in range(i + 1, 4):
                copy_digits = digits.copy()
                first_digit = digits[i]
                number = first_digit * 10 + digits[j]
                inverse_number = number % 10 * 10 + number // 10
                copy_digits.pop(j)
                copy_digits.pop(i)
                other_number = copy_digits.pop() * 10 + copy_digits.pop()
                inverse_other_number = other_number % 10 * 10 + other_number // 10
                min_sum = min(min_sum, number + other_number)
                min_sum = min(min_sum, number + inverse_other_number)
                min_sum = min(min_sum, inverse_number + other_number)
                min_sum = min(min_sum, inverse_number + inverse_other_number)
        return min_sum
