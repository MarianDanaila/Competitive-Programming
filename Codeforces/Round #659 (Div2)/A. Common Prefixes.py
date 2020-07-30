#print(chr(ord("a")+1))

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    #ans = ""
    output = []
    maxim = max(a)
    if maxim == 0:
        output.append("aaaa")
        for i in a:
            if output[-1][0] == 'z':
                el = "a"
            else:
                el = chr(ord(output[-1][0])+1)
            output.append(el * 4)
    else:
        output.append("a" * maxim)
        #print(output)
        for i in a:
            if i == maxim:
                output.append(output[-1])
            else:
                if output[-1][i] == "z":
                    el = "a"
                else:
                    el = chr(ord(output[-1][i])+1)
                if i == 0:
                    output.append(el+output[-1][i+1:])
                else:
                    output.append(output[-1][:i]+el+output[-1][i+1:])
                #print(output)
    for el in output:
        print(el)

