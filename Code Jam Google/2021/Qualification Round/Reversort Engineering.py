from itertools import permutations
t = int(input())
for test in range(1, t+1):
    n, c = [int(s) for s in input().split(" ")]
    permutation = [i for i in range(1, n+1)]
    found = False
    perm = permutations(permutation)
    perm = list(perm)
    for p in perm:
        p = list(p)
        copy_p = p.copy()
        cost = 0
        for i in range(n - 1):
            minim = i
            for j in range(i + 1, n):
                if p[j] < p[minim]:
                    minim = j
            cost += minim - i + 1
            left = i
            right = minim
            while left < right:
                p[left], p[right] = p[right], p[left]
                left += 1
                right -= 1
        if cost == c:
            print("Case #{}: {}".format(test, " ".join(map(str, copy_p))))
            found = True
            break
    if not found:
        print("Case #{}: {}".format(test, "IMPOSSIBLE"))
