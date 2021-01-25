def maxSubarraySumCircular(a):
    length_a = len(a)
    for i in range(length_a-1):
        a.append(a[i])
    print(a)
    maxim = a[0]
    sum = a[0]
    for i in range(1, len(a)):
        if sum < 0:
            sum = a[i]
        else:
            sum += a[i]
        maxim = max(sum, maxim)
    return maxim


print(maxSubarraySumCircular([5,-3,5]))