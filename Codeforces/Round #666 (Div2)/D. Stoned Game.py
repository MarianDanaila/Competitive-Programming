t = int(input())
for _ in range(t):
    ok = False
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    if max(a) > sum(a) - max(a):
        ok = True
        print('T')
    if not ok:

        if sum(a) % 2 == 0:
            print('HL')
        else:
            print('T')
