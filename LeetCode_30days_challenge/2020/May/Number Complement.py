def findComplement(num):
    new = 0
    power = 0
    while num > 0:
        if num % 2 == 0:
            new += 2 ** power
        power += 1
        num //= 2
    return new

print(findComplement(0))
