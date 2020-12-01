n = int(input())
a = [int(s) for s in input().split(" ")]
first = second = False
output = [-1] * n
for i in range(1, n):
    str1 = str(a[i-1])
    str2 = str(a[i])
    if len(str1) == len(str2):
        if len(str1) == 1:
            if str1 == '0' and str2 == '9':
                output[i - 1] = a[i - 1]
                continue
            else:
                if str1 == '0':
                    nr1 = 9
                    first = True
                    index = i
                    break
                else:
                    second = True
                    nr2 = 0
                    index = i
                    break
        else:
            nr1 = int('9'+str1[1:])
            if nr1 > int(str2):
                first = True
                index = i
                break
            else:
                nr2 = int('1'+str2[1:])
                if int(str1) > nr2:
                    second = True
                    index = i
                    break
    output[i-1] = a[i-1]
if first is False and second is False:
    print("impossible")
else:
    if first:
        output[index-1] = nr1
        output[index] = a[index]
    else:
        output[index-1] = a[index-1]
        output[index] = nr2
    for i in range(index+1, n):
        output[i] = a[i]
    # print(output)
    print(" ".join(map(str, output)))


