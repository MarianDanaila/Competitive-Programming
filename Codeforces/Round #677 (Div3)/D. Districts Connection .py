#print(" ".join(map(str,array)))
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    first = a[0]
    no = True
    for el in a:
        if el != first:
            no = False
    if no:
        print("NO")
    else:
        print("YES")
        center = a[0]
        #dct_center = set()
        for i in range(n):
            if a[i] != center:
                tail = i+1
                break
        for i in range(1, n):
            if a[i] != center:
                print(1, i+1)
            else:
                print(tail, i+1)


