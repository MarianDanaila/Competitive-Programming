t = int(input())
for i in range(t):
    piles = int(input())
    stones = [int(s) for s in input().split(" ")]
    if sum(stones) == piles:
        if piles % 2 == 0:
            print("Second")
        else:
            print("First")
    else:
        counter = 0
        for stone in stones:
            if stone == 1:
                counter += 1
            else:
                break
        if counter % 2 == 0:
            print("First")
        else:
            print("Second")