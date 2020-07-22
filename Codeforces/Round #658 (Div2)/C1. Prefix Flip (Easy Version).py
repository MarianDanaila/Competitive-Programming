# Solution1 O(n)
t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    output = ""
    changes = 0
    for i in range(n):
        if a[i] != b[i]:
            output += " " + str(i+1) + " 1 " + str(i+1)
            changes += 3
    print(str(changes) + output)


