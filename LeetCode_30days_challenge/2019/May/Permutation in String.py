from collections import Counter


def checkInclusion(self, p: str, s: str) -> bool:
    n = len(s)
    m = len(p)

    p = Counter(p)  # Convert list of anagram letters to a Counter (hashtable)

    window = None
    for i in range(0, n - m + 1):
        if i == 0:
            window = Counter(s[:m])  # Initialize window with beginning of s => length = length of anagram letters
        else:
            window[s[i - 1]] -= 1  # Move window to right: 1. remove character on the left
            window[s[i + m - 1]] += 1  # 2. add character on the right
        if len(
                window - p) == 0:  # Check if window is anagram (direct comparison of counters does not work with 0 entries)
            return True
    return False