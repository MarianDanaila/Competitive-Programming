from collections import deque
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        graph = {}
        n = len(words)
        for i in range(n - 1):
            word1 = words[i]
            len1 = len(word1)
            for j in range(i + 1, n):
                word2 = words[j]
                len2 = len(word2)
                if len2 - len1 > 1:
                    break

                if len2 == len1:
                    continue
                changes = 0
                predecessor = True
                i1 = i2 = 0
                while i1 < len1:
                    if word1[i1] != word2[i2]:
                        changes += 1
                        if changes == 2:
                            predecessor = False
                            break
                    else:
                        i1 += 1
                    i2 += 1

                if predecessor:
                    if word1 in graph:
                        graph[word1].append(word2)
                    else:
                        graph[word1] = [word2]

        max_length = 1
        visited = set()
        for word in words:
            if word not in visited:
                # run bfs
                visited.add(word)
                dq = deque()
                dq.append(word)
                length = 0
                while dq:
                    len_dq = len(dq)
                    length += 1
                    for _ in range(len_dq):
                        curr = dq.popleft()
                        if curr in graph:
                            for nxt in graph[curr]:
                                if nxt not in visited:
                                    visited.add(nxt)
                                    dq.append(nxt)

                max_length = max(max_length, length)
        return max_length
