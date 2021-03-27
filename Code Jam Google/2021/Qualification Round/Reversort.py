t = int(input())
for test in range(1, t+1):
    n = int(input())
    l = [int(s) for s in input().split(" ")]
    cost = 0
    for i in range(n-1):
        minim = i
        for j in range(i+1, n):
            if l[j] < l[minim]:
                minim = j
        cost += minim-i+1
        left = i
        right = minim
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
    print("Case #{}: {}".format(test, cost))
