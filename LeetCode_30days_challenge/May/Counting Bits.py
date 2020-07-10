def countBits(num):
    output = [0]
    for i in range(1, num + 1):
        if i & (i - 1) == 0:
            output.append(1)
        elif i % 2 == 0:
            output.append(output[i // 2])
        else:
            output.append(output[i // 2] + 1)

    return output

print(countBits(0))