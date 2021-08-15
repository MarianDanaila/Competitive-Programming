from collections import Counter, deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 1:
            if t in s:
                return t
            return ""
        counter_t = Counter(t)
        characters_s = {}
        m = len(s)
        for i in range(m):
            if s[i] not in counter_t:
                continue
            if s[i] in characters_s:
                characters_s[s[i]].append(i)
            else:
                dq = deque()
                dq.append(i)
                characters_s[s[i]] = dq

        minimum_window = m + 1
        start, end = m + 1, -1
        while True:
            curr_start, curr_end = m + 1, -1
            for ch in counter_t:
                if ch not in characters_s or len(characters_s[ch]) < counter_t[ch]:  # we can return
                    if minimum_window == m + 1:
                        return ""
                    else:
                        return s[start:end + 1]

                if characters_s[ch][0] < curr_start:
                    curr_start = characters_s[ch][0]
                    deleted = ch

                curr_end = max(characters_s[ch][counter_t[ch] - 1], curr_end)

            if curr_start < curr_end and curr_end - curr_start + 1 < minimum_window:
                minimum_window = curr_end - curr_start + 1
                start = curr_start
                end = curr_end
            characters_s[deleted].popleft()
