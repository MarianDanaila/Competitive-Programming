def isPowerOfTwo(n):
    while n % 2 == 0:
        n //= 2
    if n == 1:
        return 1
    else:
        return 0


""" 
#  with bit manipulation
return n > 0 and (n & (n-1) == 0)
"""