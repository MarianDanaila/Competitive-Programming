def rangeBitwiseAnd(x, y):
    while x < y:
        y -= (y & -y)
    return y

print(rangeBitwiseAnd(12, 15))