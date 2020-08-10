t = int(input())
for _ in range(t):
    n = int(input())
    out = ""
    for i in range(n, 0, -1):
        out += str(i) + " "
    print(out[:-1])