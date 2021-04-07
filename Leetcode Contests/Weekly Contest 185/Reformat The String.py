class Solution:
    def reformat(self, s: str) -> str:
        ch = []
        nr = []
        output = ""
        for i in s:
            if "0" <= i <= "9":
                nr.append(i)
            else:
                ch.append(i)
        if abs(len(nr)-len(ch)) <= 1:
            if len(ch) == 0:
                return s
            if len(nr) == 0:
                return s
            if len(ch) < len(nr):
                for i in range(len(ch)):
                    output += nr[i]+ch[i]
                output += nr[i+1]
            elif len(nr) < len(ch):
                for i in range(len(nr)):
                    output += ch[i]+nr[i]
                output += ch[i+1]
            else:
                for i in range(len(ch)):
                    output += nr[i]+ch[i]
        return output
