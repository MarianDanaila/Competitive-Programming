from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        unhappy = 0
        for i in range(n // 2):
            pair = pairs[i]
            bool1 = False
            bool2 = False
            for j in range(n // 2):
                if i == j:
                    continue
                another_pair = pairs[j]  # contains u,v
                if not bool1:
                    for friend in preferences[pair[0]]:
                        if friend == pair[1]:  # x prefers y
                            break
                        if friend == another_pair[0]:  # x prefers u
                            for another_friend in preferences[friend]:
                                if another_friend == another_pair[1]:  # u prefers v
                                    break
                                if another_friend == pair[0]:  # u prefers x
                                    unhappy += 1
                                    bool1 = True
                                    break
                    if not bool1:
                        for friend in preferences[pair[0]]:
                            if friend == pair[1]:  # x prefers y
                                break
                            if friend == another_pair[1]:  # x prefers u
                                for another_friend in preferences[friend]:
                                    if another_friend == another_pair[0]:  # u prefers v
                                        break
                                    if another_friend == pair[0]:  # u prefers x
                                        unhappy += 1
                                        bool1 = True
                                        break
                if not bool2:
                    for friend in preferences[pair[1]]:
                        if friend == pair[0]:  # x prefers y
                            break
                        if friend == another_pair[0]:  # x prefers u
                            for another_friend in preferences[friend]:
                                if another_friend == another_pair[1]:  # u prefers v
                                    break
                                if another_friend == pair[1]:  # u prefers x
                                    unhappy += 1
                                    bool2 = True
                                    break
                    if not bool2:
                        for friend in preferences[pair[1]]:
                            if friend == pair[0]:  # x prefers y
                                break
                            if friend == another_pair[1]:  # x prefers u
                                for another_friend in preferences[friend]:
                                    if another_friend == another_pair[0]:  # u prefers v
                                        break
                                    if another_friend == pair[1]:  # u prefers x
                                        unhappy += 1
                                        bool2 = True
                                        break
        return unhappy
