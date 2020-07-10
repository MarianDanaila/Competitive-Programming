t = int(input())
for test in range(1, t + 1):
    string = str(input())
    display =""
    for j in range(int(string[0])):
        display += "("
    for i in range(len(string) - 1):
        display += string[i]
        for j in range(int(string[i]) - int(string[i + 1])):
            display += ")"
        for j in range(int(string[i + 1]) - int(string[i])):
            display += "("
    display += string[len(string) - 1]
    for j in range(int(string[len(string) - 1])):
        display += ")"
    print("Case #{}: {}".format(test, display))

