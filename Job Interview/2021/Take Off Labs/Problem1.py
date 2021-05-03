"""
Idea:
I store in a dictionary(HashMap) the frequency of every number from the input array. I use 'buckets' array to group
numbers with the same frequency (index is the frequency). After that I traverse the 'buckets' array from end to
beginning and I put the 'k' numbers in 'most_popular' array.
"""

n = int(input())
k = int(input())
numbers = [int(s) for s in input().split(" ")]
frequency = {}
for num in numbers:
    if num not in frequency:
        frequency[num] = 1
    else:
        frequency[num] += 1

buckets = [[] for _ in range(n+1)]
for key in frequency:
    buckets[frequency[key]].append(key)

counter = 0
most_popular = []
found = False
for i in range(n, -1, -1):
    for num in buckets[i]:
        most_popular.append(num)
        counter += 1
        if counter == k:
            found = True
            break
    if found:
        break

print(most_popular)

# Input:
# 11
# 3
# 6 5 2 6 6 2 1 7 3 3 3
