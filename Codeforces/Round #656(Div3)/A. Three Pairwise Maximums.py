t = int(input())
for i in range(t):
    integers = [int(s) for s in input().split(" ")]
    x = integers[0]
    y = integers[1]
    z = integers[2]
    # cases for yes
    #if (x == y == z) or (x == y and z < y) or (y == z and x < y) or (x == z and y < x)
    if x == y == z:
        print("YES")
        print(x, y, z)
    elif x == y and z < y:
        print("YES")
        print(x, z, z)
    elif y == z and x < y:
        print("YES")
        print(x, x, y)
    elif x == z and y < x:
        print("YES")
        print(y, x, y)
    else:
        print("NO")