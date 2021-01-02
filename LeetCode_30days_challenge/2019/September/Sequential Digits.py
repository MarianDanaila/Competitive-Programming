class Solution:
    def sequentialDigits(self, low, high):
        output = []
        # FIX STARTING SEQUENTIAL NUMBER
        str_low = str(low)
        length_low = len(str_low)
        index = -1
        for i in range(length_low - 1):
            if int(str_low[i + 1]) - int(str_low[i]) > 1:
                index = 0
                break
            elif int(str_low[i + 1]) - int(str_low[i]) < 1:
                index = i + 1
                break
        special_case = False
        if index == -1:
            num = low
        elif index == 0:
            num = int(str_low[0]) + 1
            for i in range(1, length_low):
                if num % 10 == 9:
                    special_case = True
                    break
                num = num * 10 + num % 10 + 1
        else:
            num = int(str_low[:index])
            for i in range(index, length_low):
                if num % 10 == 9:
                    special_case = True
                    break
                num = num * 10 + num % 10 + 1

        if special_case:
            num = 1
            for i in range(length_low):
                num = num * 10 + num % 10 + 1

        add = int("1" * len(str(num)))
        str_first_number = ""
        for i in range(len(str(num))):
            str_first_number += str(i + 1)
        first_number = int(str_first_number)
        while True:
            if num > high:
                return output
            output.append(num)
            if num % 10 == 9:
                first_number = first_number * 10 + first_number % 10 + 1
                add = add * 10 + 1
                num = first_number
            else:
                num = num + add
