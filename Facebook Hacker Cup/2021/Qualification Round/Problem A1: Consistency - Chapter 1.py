with open("output.txt", "w") as fout:
    t = int(input())
    for test in range(1, t + 1):
        s = input()
        vowels, consonants = {}, {}
        cnt_vowels, cnt_consonants = 0, 0
        for ch in s:
            if ch in "AEIOU":
                cnt_vowels += 1
                if ch not in vowels:
                    vowels[ch] = 1
                else:
                    vowels[ch] += 1

            else:
                cnt_consonants += 1
                if ch not in consonants:
                    consonants[ch] = 1
                else:
                    consonants[ch] += 1

        max_freq_vowel, max_freq_consonant = 0, 0
        for vowel in vowels:
            max_freq_vowel = max(max_freq_vowel, vowels[vowel])

        for consonant in consonants:
            max_freq_consonant = max(max_freq_consonant, consonants[consonant])

        vowel_option = cnt_consonants + 2 * (cnt_vowels - max_freq_vowel)
        vowel_consonant = cnt_vowels + 2 * (cnt_consonants - max_freq_consonant)
        fout.write("Case #{}: {}".format(test, min(vowel_option, vowel_consonant)))
        fout.write("\n")
