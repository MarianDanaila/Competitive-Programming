class Solution:
    def modifyString(self, s: str) -> str:
        start = -1
        cnt = 0
        found = False
        arr = []
        for i in range(len(s)):
            if cnt > 0 and s[i] != '?':
                if start == -1:
                    while cnt > 0:
                        for j in range(97, 123):
                            if chr(j) != s[i]:
                                arr.append(chr(j))
                                cnt -= 1
                                if cnt == 0:
                                    break
                else:
                    while cnt > 0:
                        for j in range(97, 123):
                            if chr(j) != s[i] and chr(j) != s[start]:
                                arr.append(chr(j))
                                cnt -= 1
                                if cnt == 0:
                                    break
            if s[i] == '?':
                cnt += 1
                if not found:  # if it is the first time
                    found = True
                    start = i-1
            else:
                cnt = 0
                found = False
        if s[-1] == '?':
            while cnt > 0:
                for j in range(97, 123):
                    if chr(j) != s[start]:
                        arr.append(chr(j))
                        cnt -= 1
                        if cnt == 0:
                            break
        out = ""
        i = 0
        for ch in s:
            if ch == '?':
                out += arr[i]
                i += 1
            else:
                out += ch
        return out
