def validate_symbols(s):
    dct = {")": "(", "]": "[", "}": "{"}
    stack = []
    for i in s:
        if i is "(" or i is "{" or i is "[":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            if dct[i] == stack[len(stack)-1]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
print(validate_symbols("{[]}"))