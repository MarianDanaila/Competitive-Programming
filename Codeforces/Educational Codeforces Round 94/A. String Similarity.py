t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    out = ""
    for i in range(len(s)):
        if i % 2 == 0:
            out += s[i]
    print(out)
