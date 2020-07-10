def numJewelsInStones(j, s):
    dct = {}
    counter = 0
    for i in j:
        dct[i] = 1
    for i in s:
        try:
            if dct[i] == 1:
                counter += 1
        except KeyError:
            continue
    return counter

print(numJewelsInStones("z", "aZZ"))