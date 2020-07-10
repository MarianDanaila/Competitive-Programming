t = int(input())
for test in range(1, t + 1):
    dct = {"N": 0, "S": 0, "W": 0, "E": 0}
    string = input()
    h = 1
    w = 1
    stack = []
    multiply = 1
    for i in string:
        if "2" <= i <= "9":
            stack.append(multiply)
            multiply *= int(i)
        elif i == ")":
            multiply = stack[len(stack)-1]
            stack.pop()
        elif i == "(":
            continue
        else:
            dct[i] += multiply
    diff1 = dct["E"] - dct["W"]
    diff2 = dct["S"] - dct["N"]
    if diff1 >= 0:
        w += diff1
    else:
        w = 1000000000 + diff1 + 1

    if diff2 >= 0:
        h += diff2
    else:
        h = 1000000000 + diff2 + 1

    print("Case #{}: {} {}".format(test, w, h))

#solved only for test set 1
