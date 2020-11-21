class Solution:
    def atMostNGivenDigitSet(self, digits, n):
        dct = {}
        for i in range(len(digits)):
            dct[int(digits[i])] = i + 1
        output = [None] * len(str(n))
        str_n = str(n)
        good_digit = -1
        special_case = False
        found = False
        for i in range(len(str_n)):
            if int(str_n[i]) in dct:
                output[i] = int(str_n[i])
            elif int(digits[0]) > int(str_n[i]):
                print("DA")
                for index in range(i - 1, -1, -1):
                    if int(digits[0]) < output[index]:
                        for digit in digits:
                            if int(digit) < output[index]:
                                good_digit = int(digit)
                            else:
                                found = True
                                break
                        if found:
                            break
                if good_digit == -1:
                    special_case = True
                    break

                output[index] = good_digit

                for i in range(index + 1, len(output)):
                    output[i] = int(digits[-1])
                # return int(''.join(map(str, output)))4
                break
            else:
                for digit in digits:
                    if int(digit) < int(str_n[i]):
                        good_digit = int(digit)
                    else:
                        break
                output[i] = int(good_digit)
                for index in range(i + 1, len(str_n)):
                    output[index] = int(digits[-1])
                break
        count = 0
        if special_case:
            output = [int(digits[-1])] * (len(str_n) - 1)
        for i in range(len(output)):
            count += dct[output[i]] * (len(digits) ** (len(output) - i - 1))
        return count
