x = int(input())
y = int(input())
if 1+(x >> 31)-(-x >> 31) == 1+(y >> 31)-(-y >> 31):
    print("Same sign")
else:
    print("Different sign")