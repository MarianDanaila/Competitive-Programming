def validIPAddress(ip):
    number = 0
    word = 0
    ok = 1
    zero = 0
    if ip.count(':') == 7 and len(ip) <= 39:
        for ch in ip:
            if ('a' <= ch <= 'f') or ('A' <= ch <= 'F') or ch.isdecimal():
                word += 1
            elif ch == ':':
                if word > 4 or word == 0:
                    return "Neither"
                word = 0
            else:
                return "Neither"
        if word == 0 or word > 4:
            return "Neither"
        else:
            return "IPv6"

    elif ip.count('.') == 3 and len(ip) <= 15:
        for ch in ip:
            if '0' <= ch <= '9':
                if zero == 1:
                    return "Neither"
                if ch == '0':
                    zero = 1
                else:
                    zero = 0
                number = number * 10 + int(ch)
                ok = 0
            elif ch == '.':
                if number >= 256 or ok == 1:
                    return "Neither"
                number = 0
                ok = 1
                zero = 0
            else:
                return "Neither"
        if number >= 256 or ok == 1:
            return "Neither"
        else:
            return "IPv4"

    else:
        return "Neither"