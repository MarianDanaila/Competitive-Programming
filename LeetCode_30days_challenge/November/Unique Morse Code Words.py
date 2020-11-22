class Solution:
    def uniqueMorseRepresentations(self, words):
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        transformations = set()
        for word in words:
            transformation = []
            for ch in word:
                transformation.append(morse[ord(ch) - 97])
            transformation = "".join(transformation)
            if transformation not in transformations:
                transformations.add(transformation)
        return len(transformations)
