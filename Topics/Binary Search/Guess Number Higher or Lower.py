# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    return


class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = low + (high - low) // 2
            my_guess = guess(mid)
            if my_guess == 0:
                return mid
            elif my_guess == 1:
                low = mid + 1
            else:
                high = mid - 1
