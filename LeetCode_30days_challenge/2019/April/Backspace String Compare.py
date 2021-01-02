def replace(string):
    i = 0
    while i < len(string):
        if string[i] == "#":
            if i == 0:
                string = string[1:]
            else:
                string = string[:i - 1] + string[i + 1:]
                i -= 1
        else:
            i += 1

    return string


def backspaceCompare(S, T):
    return replace(S) == replace(T)

print(backspaceCompare("oi###mupo##rszty#s#xu###bxx##dqc#gdjz", "oi###mu#ueo##pk#o##rsztu#y#s#xu###bxx##dqc#gz#djz"))
#11aprilie