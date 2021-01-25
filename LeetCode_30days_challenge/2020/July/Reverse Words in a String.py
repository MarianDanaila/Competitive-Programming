def reverseWords(s):
    output = ""
    ans = []
    word = ""
    for i in range(len(s)-1):
        if s[i] != " ":
            word += s[i]
            if s[i+1] == " ":
                ans.append(word)
                word = ""
    if s[-1] != " ":
        word += s[-1]
        ans.append(word)
    ans.reverse()
    for i in ans:
        output += i + " "

    return output
print(reverseWords("  hello world!  "))