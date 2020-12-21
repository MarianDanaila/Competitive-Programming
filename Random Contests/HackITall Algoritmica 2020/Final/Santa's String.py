n = int(input())
s = input()
new = []
i = 0
j = n-1
while i <= j:
    if s[i] == s[j]:
        index1 = i
        index2 = j
        i += 1
        j -= 1

    elif s[i] < s[j]:
        new.append(s[i])
        i += 1
    else:
        new.append(s[j])
        j -= 1

print(''.join(new[:n]))
#ABCBCD