def stringShift(s, shift):
    suml = 0
    sumr = 0
    for i in shift:
        if i[0] == 1:
            sumr += i[1]
        else:
            suml += i[1]
    if suml < sumr:
        sh = 1
    elif suml > sumr:
        sh = 0
    else:
        return s
    print((abs(sumr-suml) % len(s)))
    s1 = len(s) - (abs(sumr-suml) % len(s))
    s2 = (abs(sumr-suml) % len(s))
    if sh == 1:
        output = s[s1:] + s[:s1]
    else:
        output = s[s2:] + s[:s2]
    return output

print(stringShift("xqgwkiqpif", [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]))