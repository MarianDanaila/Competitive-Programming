class Solution:
    def toGoatLatin(self, s):
        out = ""
        index = 0
        first = True
        vowel = False
        vowels = "aeiouAEIOU"
        first_ch = ""
        for i in range(len(s)):
            if first:
                first = False
                if s[i] in vowels:
                    vowel = True
                    out += s[i]
                else:
                    first_ch = s[i]
                    vowel = False
            else:
                if s[i] == ' ':
                    index += 1
                    first = True
                    if vowel:
                        out += "ma" + index * 'a'
                    else:
                        out += first_ch + "ma" + index * 'a'
                out += s[i]
        if vowel:
            out += "ma" + (index+1) * 'a'
        else:
            out += first_ch + "ma" + (index+1) * 'a'
        return out


sol = Solution()
print(sol.toGoatLatin("I speak Goat Latin"))