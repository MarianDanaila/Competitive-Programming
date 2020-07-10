def lonely_number(numbers):
    dct = {}
    for i in numbers:
        try:
            if dct[i] == 1:
                dct.pop(i)
        except KeyError:
            dct[i] = 1
    for i in dct:
        return i

print(lonely_number([1]))