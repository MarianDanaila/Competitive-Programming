t = int(input())
for i in range(t):
    length = int(input())
    arr = [int(s) for s in input().split(" ")]
    pos = length - 1
    while pos > 0 and arr[pos-1] >= arr[pos]:
        pos -= 1
    while pos > 0 and arr[pos-1] <= arr[pos]:
        pos -= 1
    print(pos)