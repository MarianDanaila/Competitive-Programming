with open("input.txt", "r") as fin:
    with open("output.txt", "w") as fout:
        t = int(fin.readline())
        for exercise in range(1, t + 1):
            n = int(fin.readline())
            w = fin.readline()
            hand = 0  # -1 is the left one, 1 is the right one and 0 is none
            switches = 0
            for ch in w:
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
            #print("Case #{}: {}".format(exercise, switches))
            fout.write("Case #{}: {}".format(exercise, switches))
            fout.write("\n")
