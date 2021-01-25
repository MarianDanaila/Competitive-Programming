def removeKdigits(num, k):
    if k == len(num):
        return str(0)
    output = ""
    equal = 1
    exit = 0
    for i in range(len(num)-1):
        if num[i] < num[i+1]:
            output += num[i-equal+1:i+1]
            equal = 1
        elif num[i] > num[i+1]:
            if equal >= k:
                exit = 1
                break
            else:
                k -= equal
                if k == 0:
                    exit = 1
                    break
            equal = 1
        else:
            equal += 1
    if exit:
        output += num[i-(equal-k)+1:]
        return str(int(output))
    else:
        a = len(output)-1
        output += num[-equal:]
        if num[-1] >= output[a]:
            return str(int(output[:len(output) - k]))
        else:
            return str(int(output[:len(output) - k-equal]+output[-equal:]))
print(removeKdigits("123456789", 3))