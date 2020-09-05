def getSum(n):
    sum = 0
    while n != 0:
        sum += int(n % 10)
        n //= 10

    return sum

t = int(input())
for _ in range(t):
    n, s = [int(s) for s in input().split(" ")]
    str_n = str(n)
    #sum = 0
    if getSum(n) <= s:
        print(0)
    else:
        zeroes = 0
        sum = 0
        j = 0
        for i in range(len(str_n)):
            sum += int(str_n[i])
            if sum >= s:
                break
        number = str_n[i:]
        length = len(number)
        print(10**length-int(number))
