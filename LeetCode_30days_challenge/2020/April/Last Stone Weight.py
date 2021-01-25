def lastStoneWeight(stones):
    while len(stones) > 1:
        mx1 = max(stones)
        stones.remove(mx1)
        mx2 = max(stones)
        if mx1 == mx2:
            stones.remove(mx2)
        else:
            position = stones.index(mx2)
            stones[position] = mx1 - mx2
    if len(stones) == 0:
        return 0
    else:
        return stones[0]

print(lastStoneWeight([3,2,1]))
#12aprilie