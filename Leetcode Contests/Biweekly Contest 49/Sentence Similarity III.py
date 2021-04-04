class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")
        len1 = len(s1)
        len2 = len(s2)
        start = 0
        if len1 <= len2:
            end = len2-1
            finish = True
            for i in range(len1):
                if s1[i] == s2[start]:
                    start += 1
                else:
                    finish = False
                    break
            if finish:
                return True
            for j in range(len1-1, i-1, -1):
                if s1[j] != s2[end]:
                    return False
                else:
                    end -= 1
        else:
            end = len1-1
            finish = True
            for i in range(len2):
                if s2[i] == s1[start]:
                    start += 1
                else:
                    finish = False
                    break
            if finish:
                return True
            for j in range(len2-1, i-1, -1):
                if s2[j] != s1[end]:
                    return False
                else:
                    end -= 1
        return True
