class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.curr_combination = None
        self.characters = characters
        self.combinationLength = combinationLength

    def next(self) -> str:
        if self.curr_combination is None:
            self.curr_combination = [_ for _ in range(self.combinationLength)]
        else:
            for i in range(self.combinationLength - 1, -1, -1):
                if self.curr_combination[i] != len(self.characters) + i - self.combinationLength:
                    self.curr_combination[i] += 1
                    break
            for j in range(i + 1, self.combinationLength):
                self.curr_combination[j] = self.curr_combination[j - 1] + 1

        string_combination = map(lambda x: self.characters[x], self.curr_combination)

        return "".join(list(string_combination))

    def hasNext(self) -> bool:
        return self.curr_combination != [_ for _ in
                                         range(len(self.characters) - self.combinationLength, len(self.characters))]

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
