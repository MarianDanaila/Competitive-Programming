def frequencySort(s):
    dct = {}
    output = ""
    for i in s:
        try:
            dct[i] += 1
        except KeyError:
            dct[i] = 1
    for i in sorted(dct, key=dct.get, reverse=True):
        output += i*dct[i]
    return output

frequencySort("Aabb")


