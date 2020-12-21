n, k = [int(s) for s in input().split(" ")]
c = [int(s) for s in input().split(" ")]

stack = 0
for cookie in c:
    if stack >= cookie:
        stack -= cookie
        k += 1
    else:
        stack += k-cookie
print(stack)