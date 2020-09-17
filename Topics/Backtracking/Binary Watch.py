class Solution:
    def readBinaryWatch(self, num: int):
        if num > 8:
            return []
        ones = [[[], []] for _ in range(6)]
        times = []
        for i in range(12):
            copy_i = i
            cnt = 0
            while copy_i > 0:
                copy_i = copy_i & (copy_i-1)
                cnt += 1
            ones[cnt][0].append(i)
            ones[cnt][1].append(i)
        for i in range(12, 60):
            copy_i = i
            cnt = 0
            while copy_i > 0:
                copy_i = copy_i & (copy_i-1)
                cnt += 1
            ones[cnt][1].append(i)
        i = max(num-5, 0)
        j = min(num, 5)
        while i <= j:
            for hour in ones[i][0]:
                for minute in ones[j][1]:
                    str_hour = str(hour)
                    if minute < 10:
                        str_minute = '0' + str(minute)
                    else:
                        str_minute = str(minute)
                    times.append(str_hour + ':' + str_minute)
            if i == j:
                break
            for hour in ones[j][0]:
                for minute in ones[i][1]:
                    str_hour = str(hour)
                    if minute < 10:
                        str_minute = '0' + str(minute)
                    else:
                        str_minute = str(minute)
                    times.append(str_hour + ':' + str_minute)
            i += 1
            j -= 1
        return times
