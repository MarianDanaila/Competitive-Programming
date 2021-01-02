from fractions import Fraction as f


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        up = True
        left = False
        x = y = 0
        while True:
            if x == 0 or x == p:
                if up:
                    available_height = p - y
                    if x == 0:
                        if available_height >= q:
                            y += q
                            x = p
                        else:
                            x = f(available_height*p, q)
                            y = p
                            up = False
                            left = False
                    elif x == p:
                        if available_height >= q:
                            y += q
                            x = 0
                        else:
                            x = p - f(available_height*p, q)
                            y = p
                            up = False
                            left = True
                else:
                    available_height = y
                    if x == 0:
                        if available_height >= q:
                            y -= q
                            x = p
                        else:
                            x = f(available_height*p, q)
                            y = 0
                            up = True
                            left = False
                    elif x == p:
                        if available_height >= q:
                            y -= q
                            x = 0
                        else:
                            x = p-f(available_height*p, q)
                            y = 0
                            up = True
                            left = True
            elif y == 0 or y == p:
                if not up:
                    if left:
                        y = p-f(q*x, p)
                        x = 0
                        left = False
                    else:
                        y = p-f((p-x)*q, p)
                        x = p
                        left = True
                else:
                    if left:
                        y = f(x*q, p)
                        x = 0
                        left = False
                    else:
                        y = f((p-x)*q, p)
                        x = p
                        left = True
            if x == p and y == 0:
                return 0
            elif x == p and y == p:
                return 1
            elif x == 0 and y == p:
                return 2
