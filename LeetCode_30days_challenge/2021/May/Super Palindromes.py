class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left = int(left)
        right = int(right)
        limit = 100000

        def reverse(x):
            rev = 0
            while x:
                rev = 10 * rev + x % 10
                x //= 10
            return rev

        def is_palindrome(x):
            return x == reverse(x)

        counter = 0
        # odd length
        for i in range(limit):
            first_half = str(i)
            second_half = first_half[-2::-1]
            whole = int(first_half + second_half) ** 2
            if whole > right:
                break
            if whole >= left and is_palindrome(whole):
                counter += 1

        # even length
        for i in range(limit):
            first_half = str(i)
            second_half = first_half[::-1]
            whole = int(first_half + second_half) ** 2
            if whole > right:
                break
            if whole >= left and is_palindrome(whole):
                counter += 1
        return counter
