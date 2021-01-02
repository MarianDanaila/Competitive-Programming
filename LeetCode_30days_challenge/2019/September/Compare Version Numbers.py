class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        for i in range(len(v1)):
            idx = 0
            while idx < len(v1[i]) and v1[i][idx] == '0':
                idx += 1
            if idx == len(v1[i]):
                v1[i] = '0'
            else:
                v1[i] = v1[i][idx:]
        for i in range(len(v2)):
            idx = 0
            while idx < len(v2[i]) and v2[i][idx] == '0':
                idx += 1
            if idx == len(v2[i]):
                v2[i] = '0'
            else:
                v2[i] = v2[i][idx:]
        diff = abs(len(v1) - len(v2))
        if len(v1) > len(v2):
            while diff > 0:
                v2.append('0')
                diff -= 1
        elif len(v1) < len(v2):
            while diff > 0:
                v1.append('0')
                diff -= 1
        for i in range(len(v1)):
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) > int(v2[i]):
                return 1
        return 0
