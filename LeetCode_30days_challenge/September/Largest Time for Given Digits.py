class Solution:
    def largestTimeFromDigits(self, A):
        A.sort()
        hours = []
        minutes = []
        for i in range(3):
            for j in range(i + 1, 4):
                number1 = A[i] * 10 + A[j]
                number2 = A[j] * 10 + A[i]
                if number1 < 24:
                    hours.append(number1)
                if number2 < 24:
                    hours.append(number2)
                if number1 < 60:
                    minutes.append(number1)
                if number2 < 60:
                    minutes.append(number2)
        hours.sort(reverse=True)
        minutes.sort(reverse=True)
        for hour in hours:
            for minute in minutes:
                lst = [hour // 10, hour % 10, minute // 10, minute % 10]
                lst.sort()
                if lst == A:
                    if hour < 10:
                        str_hour = '0' + str(hour)
                    else:
                        str_hour = str(hour)
                    if minute < 10:
                        str_minute = '0' + str(minute)
                    else:
                        str_minute = str(minute)
                    return str_hour + ':' + str_minute

        return ""

