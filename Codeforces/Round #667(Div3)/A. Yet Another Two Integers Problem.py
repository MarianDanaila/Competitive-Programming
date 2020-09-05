t = int(input())
for _ in range(t):
    a, b = [int(s) for s in input().split(" ")]
    if a == b:
        print(0)
    else:
        if abs(b-a) % 10 == 0:
            print(abs(b-a)//10)
        else:
            print(abs(b-a)//10 + 1)