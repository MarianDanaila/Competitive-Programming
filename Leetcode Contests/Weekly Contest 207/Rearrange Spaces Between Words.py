class Solution:
    def reorderSpaces(self, text: str) -> str:
        cnt_spaces = 0
        space = True
        words = 0
        for ch in text:
            if ch == ' ':
                cnt_spaces += 1
                space = True
            else:
                if space:
                    words += 1
                    space = False
        output = ""
        if words == 1:
            for ch in text:
                if ch != ' ':
                    output += ch
            for _ in range(cnt_spaces):
                output += ' '
        else:
            spaces_in_between = cnt_spaces // (words - 1)
            spaces_left = cnt_spaces % (words - 1)
            had_word = False
            for ch in text:
                if ch == ' ':
                    if had_word:
                        words -= 1
                        if words == 0:
                            break
                        for _ in range(spaces_in_between):
                            output += ' '
                        had_word = False
                else:
                    output += ch
                    had_word = True
            for _ in range(spaces_left):
                output += ' '
        return output
