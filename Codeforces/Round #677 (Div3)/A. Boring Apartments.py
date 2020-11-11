#print(" ".join(map(str,array)))
t = int(input())
for _ in range(t):
    x = input()
    ans = (int(x[0])-1) * 10
    if len(x) == 1:
        print(ans+1)
    elif len(x) == 2:
        print(ans+3)
    elif len(x) == 3:
        print(ans+6)
    else:
        print(ans+10)
