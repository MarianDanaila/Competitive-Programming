with open("input.txt", "r") as fin:
    with open("output.txt", "w") as fout:
        t = int(fin.readline())
        for exercise in range(1, t + 1):
            n = int(fin.readline())
            s = fin.readline()[:-1]
            hand = 0  # -1 is the left one, 1 is the right one and 0 is none
            switches = total_switches = length = 0
            dct = {}
            for ch in s:
                if ch == 'X':
                    if hand == 0:
                        hand = -1
                    if hand == 1:
                        switches += 1
                        hand = -1
                elif ch == 'O':
                    if hand == 0:
                        hand = 1
                    if hand == -1:
                        switches += 1
                        hand = 1
                if switches > 0:
                    length += 1
                    if switches in dct:
                        dct[switches] += 1
                    else:
                        dct[switches] = 1
                total_switches += switches
            ans = total_switches
            arr = []
            last = None
            for i in range(n - 1, -1, -1):
                if s[i] == 'X':
                    if not last:
                        last = 'X'
                    elif last == 'O':
                        arr.append(i)
                        last = 'X'
                elif s[i] == 'O':
                    if not last:
                        last = 'O'
                    elif last == 'X':
                        arr.append(i)
                        last = 'O'
            change = 1
            for i in range(n):
                if arr and i == arr[-1]:
                    arr.pop()
                    total_switches -= length
                    length -= dct[change]
                    change += 1
                ans += total_switches
            # remember modulo
            fout.write("Case #{}: {}".format(exercise, ans % 1000000007))
            fout.write("\n")
