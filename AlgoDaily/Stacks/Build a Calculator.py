def calculator(s):
    stack = []
    ok = 0
    number = 0
    for i in range(len(s)):
        if "0" <= s[i] <= "9":
            number *= 10
            number += int(s[i])
            if i + 1 == len(s):
                if stack[len(stack) - 1] == "+":
                    stack[len(stack) - 2] += number
                    stack.pop()
                else:
                    stack[len(stack) - 2] -= number
                    stack.pop()

            elif (s[i+1] <= "0" or s[i+1] >= "9"):
                if len(stack) == 0:
                    stack.append(number)
                else:
                    if ok == 0:
                        if stack[len(stack) - 1] == "+":
                            stack[len(stack) - 2] += number
                            stack.pop()
                        else:
                            stack[len(stack) - 2] -= number
                            stack.pop()

                    else:
                        stack.append(number)
                        ok = 0
                number = 0


        else:
            if s[i] == "(":
                ok = 1
            elif s[i] == ")":
                if len(stack) == 1:
                    continue
                if stack[len(stack)-2] == "+":
                    stack[len(stack)-3] += int(stack[len(stack)-1])
                    stack.pop()
                    stack.pop()
                else:
                    stack[len(stack)-3] -= int(stack[len(stack)-1])
                    stack.pop()
                    stack.pop()

            elif s[i] == "+" or s[i] == "-":
                stack.append(s[i])

    return stack[0]

print(calculator("(1+(4+5+2)-3)+(6+8)"))
