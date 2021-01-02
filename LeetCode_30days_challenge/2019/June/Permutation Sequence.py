from math import factorial
def getPermutation(n, k):
    output = ""
    digits = [i for i in range(1, n+1)]
    n -= 1
    fact = factorial(n)
    while n > 0:
        div = (k-1) // fact
        k = k % fact
        if k == 0:
            k = fact
        output += str(digits[div])
        digits.pop(div)
        fact //= n
        n -= 1
    return output + str(digits[0])
print(getPermutation(4, 9))