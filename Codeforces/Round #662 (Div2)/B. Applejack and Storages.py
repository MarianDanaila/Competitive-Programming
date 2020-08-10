from collections import Counter
n = int(input())
a = [int(s) for s in input().split(" ")]
q = int(input())
sides = 0
counter = Counter(a)
square = 0
for count in counter:
    sides += counter[count] - counter[count] % 2
    square += counter[count] // 4
for _ in range(q):
    event = input().split(" ")
    count = int(event[1])
    if event[0] == '+':
        counter[count] += 1
        if counter[count] % 2 == 0:
            sides += 2
        if counter[count] % 4 == 0:
            square += 1
    else:
        counter[count] -= 1
        if counter[count] % 2 == 1:
            sides -= 2
        if counter[count] % 4 == 3:
            square -= 1
    #print(sides)
    if sides >= 8 and square > 0:
        print("YES")
    else:
        print("NO")

