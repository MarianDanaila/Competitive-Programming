from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        capitalization = {}
        vowel_errors = {}
        sensitive = set()
        ans = []
        for word in wordlist:
            sensitive.add(word)
            word_lower = word.lower()
            if word_lower not in capitalization:
                capitalization[word_lower] = word

            encode = []
            for ch in word_lower:
                if ch in "aeiou":
                    encode.append('*')
                else:
                    encode.append(ch)

            encoded_word = "".join(encode)
            if encoded_word not in vowel_errors:
                vowel_errors[encoded_word] = word

        for query in queries:
            # case 1
            if query in sensitive:
                ans.append(query)
                continue

            # case 2
            query_lower = query.lower()
            if query_lower in capitalization:
                ans.append(capitalization[query_lower])
                continue

            # case 3
            encode = []
            for ch in query_lower:
                if ch in "aeiou":
                    encode.append('*')
                else:
                    encode.append(ch)
            encoded_word = "".join(encode)
            if encoded_word in vowel_errors:
                ans.append(vowel_errors[encoded_word])
                continue
            ans.append("")
        return ans
