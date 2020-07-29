with open("output.txt", "w") as fout:
    t = int(input())
    for case in range(1, t+1):
        n = int(input())
        c = input()
        a = 0
        b = 0
        for i in c:
            if i == 'A':
                a += 1
            else:
                b += 1
        #print(abs(a-b))
        if (abs(a-b)) == 1:
            fout.write("Case #{}: {}".format(case, "Y") + '\n')
            #print("Case #{}: {}".format(case, "Y"))
        else:
            fout.write("Case #{}: {}".format(case, "N") + '\n')
            #print("Case #{}: {}".format(case, "N"))