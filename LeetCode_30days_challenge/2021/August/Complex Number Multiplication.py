class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1, im1 = num1.split("+")
        r2, im2 = num2.split("+")
        r1, im1 = int(r1), int(im1[:-1])
        r2, im2 = int(r2), int(im2[:-1])
        r3 = r1 * r2 + im1 * im2 * -1
        im3 = r1 * im2 + im1 * r2
        return str(r3) + "+" + str(im3) + "i"
