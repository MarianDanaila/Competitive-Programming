t = int(input())
for _ in range(t):
    n = int(input())
    eights = (n-1) // 4 + 1
    print("9" * (n-eights) + "8" * eights)
