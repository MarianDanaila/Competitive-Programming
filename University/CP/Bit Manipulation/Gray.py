n = int(input())
for i in range(1 << n):
    binary_i = bin(i)[2:]
    print(((n-len(binary_i)) * '0') + binary_i)

