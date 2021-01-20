class Solution(object):
    def numRescueBoats(self, people, limit):
        boats = 0
        people.sort()
        i = 0
        j = len(people) - 1
        while i < j:
            if people[i] + people[j] <= limit:
                i += 1
            boats += 1
            j -= 1
        # check the last person
        if i == j:
            boats += 1
        return boats
