def canConstruct(ransomNote, magazine):
    dct = {}
    for i in magazine:
        try:
            dct[i] += 1
        except KeyError:
            dct[i] = 1
    for i in ransomNote:
        try:
            if dct[i] >= 1:
                dct[i] -= 1
            else:
                return False
        except KeyError:
            return False
    return True
