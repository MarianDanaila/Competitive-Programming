def getTV(actual, guess):
    v = 0
    t = 0
    dct = {}
    for i in range(len(actual)):
        if actual[i] == guess[i]:
            t += 1
        else:
            dct.update({actual[i]: 1})
            try:
                if dct[guess[i]] == 1:
                    v += 1
            except KeyError:
                continue
    display = str(t)+"T"+str(v)+"V"
    return display
print(getTV("130", "303"))