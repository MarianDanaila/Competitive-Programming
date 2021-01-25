from collections import deque


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        length = len(beginWord)
        dct = {}
        for word in wordList:
            for i in range(length):
                intermediate_word = word[:i] + "*" + word[i + 1:]
                if intermediate_word not in dct:
                    dct[intermediate_word] = [word]
                else:
                    dct[intermediate_word].append(word)
        dq = deque()
        dq.append([beginWord, 1])
        visited = set()
        visited.add(beginWord)
        while dq:
            curr_word, level = dq.popleft()
            for i in range(length):
                intermediate_word = curr_word[:i] + "*" + curr_word[i + 1:]

                for word in dct[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        dq.append([word, level + 1])

        return 0
