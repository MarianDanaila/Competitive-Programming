t = int(input())
for test in range(1, t+1):
    l, r = [int(s) for s in input().split(" ")]
    start = [1, 10, 101, 1010, 10101, 101010, 1010101, 10101010, 101010101, 1010101010,
             10101010101, 101010101010, 1010101010101, 10101010101010, 101010101010101,
             1010101010101010, 10101010101010101, 101010101010101010]
    end = [9, 98, 989, 9898, 98989, 989898, 9898989, 98989898, 989898989, 9898989898,
           98989898989, 989898989898, 9898989898989, 98989898989898, 989898989898989,
           9898989898989898, 98989898989898989, 989898989898989898]

    def check(nr):
        x = str(nr)
        for i in range(len(x)):
            if (i+1) % 2 == 0:  # even position
                if int(x[i]) % 2 != 0:
                    return False
            else:  # odd position
                if int(x[i]) % 2 == 0:
                    return False
        return True
    counter1 = counter2 = 0
    length_l = len(str(l))
    length_r = len(str(r))
    s_l = str(l)
    s_r = str(r)
    first = [0] * length_l
    last = [0] * length_r
    ok1 = ok2 = False
    if check(l):
        ok1 = True
        if l == start[length_l-1]:
            counter1 = 0
        else:
            for i in range(len(str(l))):
                first[i] = int(str(l)[i])
    else:
        if l <= start[length_l-1]:
            counter1 = 0
        else:
            for i in range(length_l):
                if (i + 1) % 2 == 0:  # even position
                    if int(s_l[i]) % 2 != 0:
                        index = i
                        break
                else:  # odd position
                    if int(s_l[i]) % 2 == 0:
                        index = i
                        break
                first[i] = int(s_l[i])
            first[i] = int(s_l[i])
            # we need to populate the last elements after with '98'
            if (index+1) % 2 != 0 and first[index] == 0:
                first[index] = 9
                for i in range(index-1, -1, -1):
                    if (i+1) % 2 == 0:
                        if first[i] == 0:
                            first[i] = 8
                        else:
                            first[i] -= 2
                            break
                    else:
                        if first[i] == 1:
                            first[i] = 9
                        else:
                            first[i] -= 2
                            break
            else:
                first[index] -= 1
            for i in range(index+1, length_l):
                if (i+1) % 2 == 0:
                    first[i] = 8
                else:
                    first[i] = 9
    if check(r):
        ok2 = True
        if r == end[length_r - 1]:
            counter2 = 0
        else:
            for i in range(len(str(r))):
                last[i] = int(str(r)[i])

    else:
        if r >= end[length_r - 1]:
            counter2 = 0
        else:
            for i in range(length_r):
                if (i + 1) % 2 == 0:  # even position
                    if int(s_r[i]) % 2 != 0:
                        index = i
                        break
                else:  # odd position
                    if int(s_r[i]) % 2 == 0:
                        index = i
                        break
                last[i] = int(s_r[i])
            last[i] = int(s_r[i])

            # we need to populate the last elements after with '98'

            if (index + 1) % 2 != 0 and last[index] == 0:
                last[index] = 9
                for i in range(index - 1, -1, -1):
                    if (i + 1) % 2 == 0:
                        if last[i] == 0:
                            last[i] = 8
                        else:
                            last[i] -= 2
                            break
                    else:
                        if last[i] == 1:
                            last[i] = 9
                        else:
                            last[i] -= 2
                            break
            else:
                last[index] -= 1
            for i in range(index + 1, length_l):
                if (i + 1) % 2 == 0:
                    last[i] = 8
                else:
                    last[i] = 9
    # print(first, last)
    beetween = 0
    for digit in range(1, length_r+1):
        beetween += 5 ** digit
    # print(beetween)
    for i in range(len(first)):
        counter1 += (first[i]//2+1) * (5 ** (len(first)-i-1))

    if ok1:
        counter1 -= 1
    # print(counter1)
    for i in range(len(last)):
        counter2 += (last[i]//2+1) * (5 ** (len(last) - i-1))
    # print(counter2)
    ans = counter2-counter1

    print("Case #{}: {}".format(test, ans))
