from math import log2
t = int(input())
for _ in range(t):
    n = int(input())
    if n & (n - 1) == 0 and n > 1:  # if n is perfect square
        if log2(n) % 2 == 0:
            print("Alice")
        else:
            print("Bob")
    elif n % 2 == 1:
        print("Bob")
    else:
        print("Alice")
